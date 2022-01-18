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
import com.neuromeka.fryingtemplatapp.data.ModbusData;
import com.neuromeka.fryingtemplatapp.util.NRMKLog;

import de.re.easymodbus.modbusclient.ModbusClient;


/**
 * 
 * @author guhee.jung
 */
public class ReadMultiModbus extends Thread {

	public static final int CONNECTION_FAILED 		= 0;
	public static final int CONNECTION_SUCCESS 		= 1;

	private ModbusClient modbusClient;

	private Handler handler;
	private int startAddress;
	private int dataLen;
	private Message msg;

	public ReadMultiModbus(Handler $handler, int $startAddress, int $dataLen){

		handler 		= $handler;
		startAddress	= $startAddress;
		dataLen			= $dataLen;
	};
	
	public void run(){

//		NRMKLog.log("[ReadModbus] Target step address : " + MainApplication.mainData.getRobotIp() + " : " + Config.SERVER_PORT);

		try{

			modbusClient = new ModbusClient();
			modbusClient.Connect(MainApplication.mainData.getRobotIp(), Config.SERVER_PORT);

			if(modbusClient.isConnected() == false){

				msg 		= handler.obtainMessage();
				msg.arg1 	= CONNECTION_FAILED;
				handler.sendMessage(msg);
				return;
			}

			try{
				int[] readData = modbusClient.ReadHoldingRegisters(startAddress, dataLen);

				msg 		= handler.obtainMessage();
				msg.arg1 	= CONNECTION_SUCCESS;
				msg.obj 	= new ModbusData(startAddress, readData);
				handler.sendMessage(msg);

			}catch(Exception e){

				NRMKLog.log("[ReadModbus] Modbus read error : " + e.getMessage());
			}

		}catch (Exception e) {

			NRMKLog.log("[ReadModbus] Modbus connection error : " + e.getMessage());

			msg 		= handler.obtainMessage();
			msg.arg1 	= CONNECTION_FAILED;
			handler.sendMessage(msg);

		}//if
	}
}
