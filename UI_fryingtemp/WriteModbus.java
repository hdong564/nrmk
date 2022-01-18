/* NRMKFoundation, Copyright 2014- Neuromeka. All rights reserved.
 *
 * This library is commercial and cannot be redistributed, and/or modified
 * WITHOUT ANY ALLOWANCE OR PERMISSION OF Neuromeka
 */

package com.neuromeka.fryingtemplatapp.comm;

import android.os.Handler;


import com.neuromeka.fryingtemplatapp.MainApplication;
import com.neuromeka.fryingtemplatapp.data.Config;
import com.neuromeka.fryingtemplatapp.util.NRMKLog;

import de.re.easymodbus.modbusclient.ModbusClient;


/**
 * 
 * @author guhee.jung
 */
public class WriteModbus extends Thread {

	public static final int CONNECTION_FAIL 	= -1;
	public static final int WRITING_FAIL 		= 0;

	private ModbusClient modbusClient;

	private Handler hander;
	private int address;
	private int value;


	public WriteModbus(Handler $handler, int $address, int $value){

		hander 	= $handler;
		address	= $address;
		value	= $value;
	};
	
	public void run(){

		NRMKLog.log("[WriteModbus] Target step address : " + MainApplication.mainData.getRobotIp() + " : " + Config.SERVER_PORT);

		try{

			modbusClient = new ModbusClient();
			modbusClient.Connect(MainApplication.mainData.getRobotIp(), Config.SERVER_PORT);

			try{
				modbusClient.WriteSingleRegister(address, value);

				NRMKLog.log("[WriteModbus] Write value : " + address + " | " + value);

			}catch(Exception e){

				NRMKLog.log("[WriteModbus] Modbus writing error : " + e.getMessage());
			}

		}catch (Exception e) {

			NRMKLog.log("[WriteModbus] Modbus connection error : " + e.getMessage());
			e.printStackTrace();

		}
	}


}
