class ShmWrapper(object):
    def __init__(self, name, flags=0):
        try:
            self.shm = SharedMemory(name, flags=flags)
        except:
            print("Share memory '%s' open error" % name)
            sys.exit(-1)
        # self.offset = offset + INDY_SHM_MGR_OFFSET
        # self.size = size
        # print("Shared Memory:", name, self.offset, size)

    def read(self, offset, size):
        self.offset = offset + INDY_SHM_MGR_OFFSET
        self.size = size

        lseek(self.shm.fd, self.offset, SEEK_SET)
        return read(self.shm.fd, self.size)

    def write(self, offset, data=None):
        self.offset = offset + INDY_SHM_MGR_OFFSET
        lseek(self.shm.fd, self.offset, SEEK_SET)
        if data is None:
            return write(self.shm.fd, '1'.encode())
        else:
            return write(self.shm.fd, data)

    def close(self):
        self.shm.close_fd()


class IndyShmCommand:
    def __init__(self, sync_mode=False, joint_dof=6):
        self.joint_dof = joint_dof
        self.sync_mode = sync_mode
        self.shm = ShmWrapper(INDY_SHM_NAME)

    def shm_access(self, shm_name, data_size, data_type=''):
        # shm = ShmWrapper(INDY_SHM_NAME, shm_name, data_size)
        if len(data_type) == 0:
            val = self.shm.read(shm_name, data_size)
        else:
            val = list(unpack(data_type, self.shm.read(shm_name, data_size)))
        if len(val) == 1:
            val = val[0]
        # shm.close()
        return val

    def shm_command(self, shm_name, data_size=1, data_type='', shm_data=None):
        # shm = ShmWrapper(INDY_SHM_NAME, shm_name, data_size)
        if len(data_type) == 0:
            ret = self.shm.write(shm_name, shm_data)
        else:
            if type(shm_data) == list:
                ret = self.shm.write(shm_name, pack(data_type, *shm_data))
            else:
                ret = self.shm.write(shm_name, pack(data_type, shm_data))
        # shm.close()
        return ret