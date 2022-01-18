package com.neuromeka.fryingtemplatapp;

import android.annotation.SuppressLint;
import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.os.Message;

import androidx.annotation.NonNull;

import com.neuromeka.fryingtemplatapp.comm.ReadMultiModbus;
import com.neuromeka.fryingtemplatapp.comm.WriteMultiModbus;
import com.neuromeka.fryingtemplatapp.data.ModbusData;
import com.neuromeka.fryingtemplatapp.util.NRMKLog;

import java.util.Timer;
import java.util.TimerTask;

public class MainService extends Service {

    private final IBinder serviceBinder = new ServiceBinder();
    private ServiceCallback serviceCallback;

    private TimerTask stateTimerTask;
    private Timer stateTimer;
    private boolean isConnected = false;


    public MainService() {
    }

    @Override
    public IBinder onBind(Intent intent) {

        return serviceBinder;
    }

    /**
     * 서비스 생성
     */
    @Override
    public void onCreate() {

        super.onCreate();

        stateTimerTask = new TimerTask() {
            @Override
            public void run() {

                readMultiModbusData(ModbusData.ADDRESS_REALTIME_STATE, 50);
                readMultiModbusData(ModbusData.ADDRESS_SETTING_BTN_STATE, 6);
            }
        };

        NRMKLog.log("[MainService] onCreate");
    }

    @SuppressLint("HandlerLeak")
    private void readMultiModbusData(int $startAddress, int $dataLen){

        new ReadMultiModbus(new Handler(Looper.getMainLooper()){

            @Override
            public void handleMessage(@NonNull Message msg) {
                super.handleMessage(msg);

                switch(msg.arg1){

                    case ReadMultiModbus.CONNECTION_SUCCESS:

                        //첫 통신 성공 시, 레시피 정보 일괄 업데이트
                        if(isConnected == false) {

                            isConnected = true;
                            serviceCallback.sendRecipe();
                        }

                        serviceCallback.updateRealTimeData((ModbusData)msg.obj);
                        break;

                    case ReadMultiModbus.CONNECTION_FAILED:

                        isConnected = false;
                        serviceCallback.connectionFailed();
                        break;
                }
            }
        }, $startAddress, $dataLen).start();
    }

    /**
     * 단일 모드 버스 데이터 write
     */
    public void writeMultiModbusData(int $modbusStartAddress, int[] $values){

        new WriteMultiModbus(new Handler(Looper.getMainLooper()) {

            @Override
            public void handleMessage(Message msg) {

                super.handleMessage(msg);

                switch (msg.arg1) {

                    case WriteMultiModbus.CONNECTION_FAILED:

                        if(serviceCallback != null)
                            serviceCallback.connectionFailed();

                        break;

                    case WriteMultiModbus.WRITING_FAILED:

                        if(serviceCallback != null)
                            serviceCallback.writeFailed();
                        break;
                }

            }
        }, $modbusStartAddress, $values).start();
    }

    /**
     * 서비스 소멸
     */
    @Override
    public void onDestroy() {

        super.onDestroy();

        disposeStateTimer();
        NRMKLog.log("[MainService] onDestroy");
    }

    /**
     * 상태 호출 타이머 시작
     */
    public void startStateTimer(){

        if(stateTimer != null)
            stateTimer.cancel();

        stateTimer = new Timer();
        stateTimer.schedule(stateTimerTask, 0, 500);
    }

    /**
     * 상태 호출 타이머 종료
     */
    public void disposeStateTimer(){

        if(stateTimerTask != null)
            stateTimerTask.cancel();

        if(stateTimer != null)
            stateTimer.cancel();
    }

    public void registerCallback(ServiceCallback $callback){

        serviceCallback = $callback;
    }

    //==============================================================================
    //=================================== class ====================================
    /**
     * 서비스 바인딩 클래스
     */
    public class ServiceBinder extends Binder {

        public MainService getService(){

            return MainService.this;
        }

    }//class


    //==============================================================================
    //================================ interface ===================================
    /**
     * service -> activity 콜백 인터페이스
     */
    public interface ServiceCallback{

        public void updateRealTimeData(ModbusData $modbusData);
        public void sendRecipe();
        public void connectionFailed();
        public void writeFailed();
    }

}//class