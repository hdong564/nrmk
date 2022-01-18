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

import de.re.easymodbus.modbusclient.ModbusClient;


/**
 * 
 * @author guhee.jung
 */
public class ReadModbus extends Thread {

	public static final int CONNECTION_FAIL 	= -1;
	public static final int READING_FAIL 		= 0;
	public static final int READING_INFO 		= 1;

	private ModbusClient modbusClient;

	private Handler handler;
	private int address;
	private Message msg;

	public ReadModbus(Handler $handler, int $address){

		handler 	= $handler;
		address		= $address;
	};
	
	public void run(){

		NRMKLog.log("[ReadModbus] Target step address : " + MainApplication.mainData.getRobotIp() + " : " + Config.SERVER_PORT);

		try{

			modbusClient = new ModbusClient();
			modbusClient.Connect(MainApplication.mainData.getRobotIp(), Config.SERVER_PORT);

			try{
				int readData = modbusClient.ReadHoldingRegisters(address, 1)[0];
				NRMKLog.log("[ReadModbus] Read data : " + address + " | " + readData);

//				CommData commData = new CommData(address);
//				commData.setData1(readData);
//
//				msg 		= handler.obtainMessage();
//				msg.arg1 	= READING_INFO;
//				msg.obj 	= commData;
//				handler.sendMessage(msg);

			}catch(Exception e){

				NRMKLog.log("[ReadModbus] Modbus read error : " + e.getMessage());
			}

		}catch (Exception e) {

			NRMKLog.log("[ReadModbus] Modbus connection error : " + e.getMessage());
			e.printStackTrace();

		}
	}


}
