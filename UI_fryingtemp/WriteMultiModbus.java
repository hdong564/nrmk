/* NRMKFoundation, Copyright 2014- Neuromeka. All rights reserved.
 *
 * This library is commercial and cannot be redistributed, and/or modified
 * WITHOUT ANY ALLOWANCE OR PERMISSION OF Neuromeka
 */

package com.neuromeka.fryingtemplatapp.comm;

import android.os.Handler;
import android.os.Message;

import com.neuromeka.fryingtemplatapp.MainApplication;
import com.neuromeka.fryingtemplatapp.data.Config;
import com.neuromeka.fryingtemplatapp.util.NRMKLog;

import java.util.Arrays;

import de.re.easymodbus.modbusclient.ModbusClient;


/**
 * 
 * @author guhee.jung
 */
public class WriteMultiModbus extends Thread {

	public static final int CONNECTION_FAILED 	= -1;
	public static final int WRITING_FAILED 		= 0;

	private ModbusClient modbusClient;

	private Handler handler;
	private String ipAddress;
	private int startAddress;
	private int[] values;

	private Message msg;



	public WriteMultiModbus(Handler $handler, int $startAddress, int[] $values){

		handler			= $handler;
		startAddress	= $startAddress;
		values			= $values;
	};
	
	public void run(){

//		NRMKLog.log("[WriteMultiModbus] Target step address : " + ipAddress + " : " + Config.SERVER_PORT);

		try{

			modbusClient = new ModbusClient();
			modbusClient.Connect(MainApplication.mainData.getRobotIp(), Config.SERVER_PORT);

			try{
				modbusClient.WriteMultipleRegisters(startAddress, values);

				NRMKLog.log("[WriteMultiModbus] Write value : " + startAddress + " | " + Arrays.toString(values));

			}catch(Exception e){

//				NRMKLog.log("[WriteMultiModbus] Modbus writing error : " + e.getMessage());

				msg 		= handler.obtainMessage();
				msg.arg1 	= WRITING_FAILED;
				handler.sendMessage(msg);
			}

		}catch (Exception e) {

//			NRMKLog.log("[WriteMultiModbus] Modbus connection error : " + e.getMessage());

			msg 		= handler.obtainMessage();
			msg.arg1 	= CONNECTION_FAILED;
			handler.sendMessage(msg);

		}
	}


}
