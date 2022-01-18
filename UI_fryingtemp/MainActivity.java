package com.neuromeka.fryingtemplatapp;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.app.Activity;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.os.Bundle;
import android.os.IBinder;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.TextView;
import android.widget.Toast;

import com.neuromeka.fryingtemplatapp.adapter.ImageSliderAdapter;
import com.neuromeka.fryingtemplatapp.data.Config;
import com.neuromeka.fryingtemplatapp.data.ModbusData;
import com.neuromeka.fryingtemplatapp.data.RecipeData;
import com.neuromeka.fryingtemplatapp.display.BasketView;
import com.neuromeka.fryingtemplatapp.display.FryerView;
import com.neuromeka.fryingtemplatapp.display.ShakingOptionView;
import com.neuromeka.fryingtemplatapp.display.SliderItem;
import com.neuromeka.fryingtemplatapp.listener.ShakingOptionBtnCallback;
import com.neuromeka.fryingtemplatapp.listener.YesNoDialogListener;
import com.neuromeka.fryingtemplatapp.popup.RecipeListPopup;
import com.neuromeka.fryingtemplatapp.popup.YesNoPopupDialog;
import com.neuromeka.fryingtemplatapp.util.NRMKLog;
import com.neuromeka.fryingtemplatapp.util.SharedPrefManager;
import com.neuromeka.fryingtemplatapp.util.Util;
import com.google.android.material.textfield.TextInputEditText;
import com.smarteist.autoimageslider.IndicatorView.animation.type.IndicatorAnimationType;
import com.smarteist.autoimageslider.SliderAnimations;
import com.smarteist.autoimageslider.SliderView;
import com.warkiz.widget.IndicatorSeekBar;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private final static int[] FRYER_VIEW_ID_LIST           = {R.id.fryer1, R.id.fryer2, R.id.fryer3, R.id.fryer4};
    private final static int[] BASKET_VIEW_ID_LIST          = {R.id.basket1, R.id.basket2, R.id.basket3, R.id.basket4, R.id.basket5, R.id.basket6, R.id.basket7, R.id.basket8};
    private final static int[] SHAKING_OPTION_VIEW_ID_LIST  = {R.id.shakingOption1, R.id.shakingOption2, R.id.shakingOption3};
    private final static int[] SLIDER_IMAGE_ID_LIST         = {R.drawable.slide_img_0, R.drawable.slide_img_1, R.drawable.slide_img_2, R.drawable.slide_img_3};

    private MainService mainService;
    private Activity activity;

    private ArrayList<TextView> menuBtnList;

    private ConstraintLayout tutorialMenuUI;
    private ConstraintLayout workMenuUI;
    private ConstraintLayout recipeMenuUI;
    private ConstraintLayout settingMenuUI;
    private ArrayList<ConstraintLayout> menuUIList;

    private TextView ipAddressTxt;
    private TextView robotStateTxt;
    private TextView runningTimeTxt;
    private TextView workCountTxt;
    private TextView workStateTxt;

    //튜토리얼 메뉴 UI =================================
    private SliderView imageSlider;
    private ImageSliderAdapter imageSliderAdapter;


    //실행 메뉴 UI =====================================
    private ArrayList<FryerView> fryerViewList;
    private ArrayList<BasketView> basketViewList;



    //레시피 UI ========================================
    private ArrayList<ShakingOptionView> shakingOptionViewList;

    private ConstraintLayout step1PointUI;
    private ConstraintLayout step2PointUI;
    private ConstraintLayout step3PointUI;

    private TextView step1PointInfoTxt;
    private TextView step2PointInfoTxt;
    private TextView step3PointInfoTxt;

    private View scheduleBar;
    private int scheduleBarWidth;
    private float scheduleBarPosX;

    private TextInputEditText recipeNameInputTxt;
    private TextInputEditText recipeTimeMinuteInputTxt;
    private TextInputEditText recipeTimeSecondInputTxt;

    private IndicatorSeekBar deoilSlider;

    private TextView endTimeTxt;

    private int recipeTotalTime = 0;

    private TextInputEditText ipInputTxt;

    //설정 UI ========================================
    private TextView directTeachingOnBtn;
    private TextView directTeachingOffBtn;
    private TextView gripperOnBtn;
    private TextView gripperOffBtn;
    private TextView playBtn;
    private TextView pauseBtn;
    private TextView stopBtn;
    private TextView resumeBtn;
    private TextView moveToHomePosBtn;
    private TextView moveToZeroPosBtn;
    private TextView moveToPackagePosBtn;


    private int directTeachingBtnStatePrev  = -1;
    private int gripperBtnStatePrev         = -1;
    private int programBtnStatePrev         = -1;




    //팝업 액티비티 런처
    private ActivityResultLauncher<Intent> popupLauncher;




    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //registerForActivityResult는 OnStart 실행전에 수행되어야 함.
        initPopupLauncher();

        activity = this;
        checkPermission();
    }

    /**
     * 앱 시작시, 사용 권한에 대한 사용자 확인 절차를 진행한다.
     */
    private void checkPermission() {

        //권한인 없을 경우,
        if(ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED){

            ActivityCompat.requestPermissions(  this, Config.PERMISSION_LIST, Config.MY_PERMISSIONS_REQUEST_READ_CONTACTS);

        }else{

            init();
        }
    }//func

    /**
     * 사용자 권한 설정 확인 피드백
     * @param requestCode
     * @param permissions
     * @param grantResults
     */
    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults){

        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        switch(requestCode) {

            case Config.MY_PERMISSIONS_REQUEST_READ_CONTACTS:
            {
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    init();

                } else {

                    Toast.makeText(this, "권한 사용 동의 후 사용이 가능합니다.", Toast.LENGTH_LONG).show();
                    finish();
                }
            }
            break;
        }
    }//func

    private void init() {

        // 실제 사용되는 디바이스 화면 사이즈 저장 ===================================
//        DisplayMetrics displaymetrics = activity.getApplicationContext().getResources().getDisplayMetrics();
//        NRMKLog.log("Screen resolution : " + displaymetrics.widthPixels + " x " + displaymetrics.heightPixels);
        //============================================================================

        MainApplication.mainData.setRobotIp(SharedPrefManager.getInstance(activity).getRobotIP());

        initUI();
        initService();

        //앱 시작시, 로컬 저장된 레시피 파일 정보 한번 read
        Util.readRecipeFile(this);

        selectMenu(R.id.cookingMenuBtn);
    }

    private void initPopupLauncher(){

        popupLauncher = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                new ActivityResultCallback<ActivityResult>() {
                    @Override
                    public void onActivityResult(ActivityResult result) {

                        if(result.getResultCode() == RESULT_OK){

                            int popupId = result.getData().getIntExtra(Config.POPUP_ID, -1);

                            switch(popupId){

                                case Config.POPUP_ID_ASK_FIN_COOKING:

                                    int dataIndex = result.getData().getIntExtra(Config.YES_NO_POPUP_DATA_INDEX, -1);
                                    NRMKLog.log(String.valueOf(dataIndex) + "번 슬롯 조리 종료하기");
                                    break;

                                case Config.POPUP_ID_RECIPE_SAVE:

                                    int saveIndex = result.getData().getIntExtra(Config.RECIPE_POPUP_INTENT_ITEM_INDEX, -1);

                                    saveRecipeData(saveIndex);
                                    break;

                                case Config.POPUP_ID_RECIPE_LOAD:

                                    int loadIndex = result.getData().getIntExtra(Config.RECIPE_POPUP_INTENT_ITEM_INDEX, -1);

                                    loadRecipeData(loadIndex);
                                    break;

                                case Config.POPUP_ID_CANCEL_RECIPE_SELECTION:

                                    int cancelSlotIndex = result.getData().getIntExtra(Config.RECIPE_POPUP_INTENT_SLOT_INDEX, -1);
                                    mainService.writeMultiModbusData(ModbusData.ADDRESS_CANCEL_MENU_SELECTION_CMD, new int[]{cancelSlotIndex + 1});
                                    mainService.writeMultiModbusData(ModbusData.ADDRESS_BASKET1_RECIPE_REGISTER + cancelSlotIndex, new int[]{0});
                                    mainService.writeMultiModbusData(ModbusData.ADDRESS_BASKET1_RECIPE_CHANGE + cancelSlotIndex, new int[]{0});

                                    Util.showShortToast(activity,String.valueOf(cancelSlotIndex + 1) + "번 바스켓의 메뉴 선택을 취소하였습니다.");
                                    break;

                                case Config.POPUP_ID_RECIPE_SELECT:

                                    int slotIndex   = result.getData().getIntExtra(Config.RECIPE_POPUP_INTENT_SLOT_INDEX, -1);
                                    int recipeIndex = result.getData().getIntExtra(Config.RECIPE_POPUP_INTENT_ITEM_INDEX, -1);

                                    selectRecipeToBasket(slotIndex, recipeIndex);
                                    break;

                            }
                        }
                    }
                });
    }

    private void initHeaderUI(){

        ipAddressTxt    = (TextView)findViewById(R.id.ipTxt);
        ipAddressTxt.setText(getResources().getString(R.string.header_ip_label) + " " + MainApplication.mainData.getRobotIp());

        robotStateTxt   = (TextView)findViewById(R.id.robotStateTxt);
        runningTimeTxt  = (TextView)findViewById(R.id.workTimeTxt);
        workCountTxt    = (TextView)findViewById(R.id.workCountTxt);
        workStateTxt    = (TextView)findViewById(R.id.workStateTxt);
    }

    private void initSettingUI(){

        ipInputTxt      = (TextInputEditText)findViewById(R.id.robotIPEditTxt);
        ipInputTxt.setText(MainApplication.mainData.getRobotIp());

        directTeachingOnBtn     = (TextView)findViewById(R.id.directTeachingOnBtn);
        directTeachingOffBtn    = (TextView)findViewById(R.id.directTeachingOffBtn);
        gripperOnBtn            = (TextView)findViewById(R.id.gripperOnBtn);
        gripperOffBtn           = (TextView)findViewById(R.id.gripperOffBtn);

        playBtn                 = (TextView)findViewById(R.id.playProgramBtn);
        pauseBtn                = (TextView)findViewById(R.id.pauseProgramBtn);
        stopBtn                 = (TextView)findViewById(R.id.stopProgramBtn);
        resumeBtn               = (TextView)findViewById(R.id.resumeProgramBtn);

        moveToHomePosBtn        = (TextView)findViewById(R.id.moveToHomePosBtn);
        moveToHomePosBtn.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {

                switch (motionEvent.getAction()){

                    case MotionEvent.ACTION_DOWN:

                        moveToHomePosBtn.setPressed(true);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_HOME_POS_CMD, new int[]{1});
                        break;

                    case MotionEvent.ACTION_UP:

                        moveToHomePosBtn.setPressed(false);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_HOME_POS_CMD, new int[]{0});
                        break;
                }
                return true;
            }
        });

        moveToZeroPosBtn        = (TextView)findViewById(R.id.moveToZeroPosBtn);
        moveToZeroPosBtn.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {

                switch (motionEvent.getAction()){

                    case MotionEvent.ACTION_DOWN:

                        moveToZeroPosBtn.setPressed(true);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_ZERO_POS_CMD, new int[]{1});
                        break;

                    case MotionEvent.ACTION_UP:

                        moveToZeroPosBtn.setPressed(false);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_ZERO_POS_CMD, new int[]{0});
                        break;
                }
                return true;
            }
        });

        moveToPackagePosBtn    = (TextView)findViewById(R.id.moveToPackagePosBtn);
        moveToPackagePosBtn.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {

                switch (motionEvent.getAction()){

                    case MotionEvent.ACTION_DOWN:

                        moveToPackagePosBtn.setPressed(true);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_PACKAGE_POS_CMD, new int[]{1});
                        break;

                    case MotionEvent.ACTION_UP:

                        moveToPackagePosBtn.setPressed(false);
                        mainService.writeMultiModbusData(ModbusData.ADDRESS_MOVE_TO_PACKAGE_POS_CMD, new int[]{0});
                        break;
                }
                return true;
            }
        });
    }

    private void initUI(){

        initHeaderUI();
        initSettingUI();


        int len, i;

        menuBtnList     = new ArrayList<TextView>();
        menuBtnList.add((TextView)findViewById(R.id.tutorialMenuBtn));
        menuBtnList.add((TextView)findViewById(R.id.cookingMenuBtn));
        menuBtnList.add((TextView)findViewById(R.id.recipeMenuBtn));
        menuBtnList.add((TextView)findViewById(R.id.settingMenuBtn));

        menuUIList     = new ArrayList<ConstraintLayout>();
        menuUIList.add(tutorialMenuUI   = (ConstraintLayout) findViewById(R.id.tutorialUI));
        menuUIList.add(workMenuUI       = (ConstraintLayout) findViewById(R.id.workUI));
        menuUIList.add(recipeMenuUI     = (ConstraintLayout) findViewById(R.id.recipeUI));
        menuUIList.add(settingMenuUI    = (ConstraintLayout) findViewById(R.id.settingUI));

        scheduleBar  = (View) findViewById(R.id.baseArea);
        scheduleBar.post(new Runnable() {
            @Override
            public void run() {

                scheduleBarWidth    = scheduleBar.getWidth();
                scheduleBarPosX     = scheduleBar.getX();
            }
        });

        step1PointUI        = (ConstraintLayout)findViewById(R.id.step1PointUI);
        step1PointInfoTxt   = (TextView)findViewById(R.id.step1PointTxt);
        step1PointUI.setVisibility(View.INVISIBLE);

        step2PointUI        = (ConstraintLayout)findViewById(R.id.step2PointUI);
        step2PointInfoTxt   = (TextView)findViewById(R.id.step2PointTxt);
        step2PointUI.setVisibility(View.INVISIBLE);

        step3PointUI        = (ConstraintLayout)findViewById(R.id.step3PointUI);
        step3PointInfoTxt   = (TextView)findViewById(R.id.step3PointTxt);
        step3PointUI.setVisibility(View.INVISIBLE);

        recipeNameInputTxt  = (TextInputEditText)findViewById(R.id.recipeNameEditTxt);

        recipeTimeMinuteInputTxt  = (TextInputEditText)findViewById(R.id.recipeTimeMinuteEditTxt);
        recipeTimeMinuteInputTxt.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {}

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

                updateRecipeTimeUI();
            }

            @Override
            public void afterTextChanged(Editable editable) {}
        });

        recipeTimeSecondInputTxt  = (TextInputEditText)findViewById(R.id.recipeTimeSecondEditTxt);
        recipeTimeSecondInputTxt.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {}

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

                if(charSequence.toString().length() > 0 && Integer.parseInt(charSequence.toString()) > 59)
                    recipeTimeSecondInputTxt.setText("59");

                updateRecipeTimeUI();
            }

            @Override
            public void afterTextChanged(Editable editable) {}
        });

        imageSlider = findViewById(R.id.tutorialImageSlider);

        imageSlider.post(new Runnable() {
            @Override
            public void run() {

                NRMKLog.log("slider size : " + imageSlider.getWidth() + " / " + imageSlider.getHeight());

            }
        });

        SliderItem sliderItem;
        List<SliderItem> sliderItemList = new ArrayList<SliderItem>();
        len = SLIDER_IMAGE_ID_LIST.length;

        for(i = 0; i < len; i++){

            sliderItem = new SliderItem();
            sliderItem.setImageUrl(SLIDER_IMAGE_ID_LIST[i]);
            sliderItemList.add(sliderItem);
        }

        imageSliderAdapter = new ImageSliderAdapter(this);
        imageSliderAdapter.renewItems(sliderItemList);

        imageSlider.setSliderAdapter(imageSliderAdapter);
        imageSlider.setIndicatorAnimation(IndicatorAnimationType.WORM);
        imageSlider.setSliderTransformAnimation(SliderAnimations.SIMPLETRANSFORMATION);
        imageSlider.setIndicatorSelectedColor(Color.WHITE);
        imageSlider.setIndicatorUnselectedColor(Color.GRAY);


        // Fryer 슬롯 정의 =====================================================
        len = FRYER_VIEW_ID_LIST.length;
        fryerViewList = new ArrayList<FryerView>();
        FryerView fryerView;

        for(i = 0; i < len; i++) {

            fryerView = (FryerView) findViewById(FRYER_VIEW_ID_LIST[i]);
            fryerView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    FryerView fryerViewSlot = (FryerView) view;

                    if(fryerViewSlot.getSlotState() != FryerView.STATE_EMPTY)
                        openCookingYesNoPopup(fryerViewSlot.getSlotIndex());
                }
            });


            fryerViewList.add(fryerView);
        }

        // basket 슬롯 정의 =====================================================
        len = BASKET_VIEW_ID_LIST.length;
        basketViewList = new ArrayList<BasketView>();
        BasketView basketView;

        for(i = 0; i < len; i++) {

            basketView = (BasketView) findViewById(BASKET_VIEW_ID_LIST[i]);
            basketView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    BasketView basketViewSlot = (BasketView) view;
                    if(basketViewSlot.getState() == BasketView.STATE_DONE)return;

//                    NRMKLog.log("basket click : " + String.valueOf(basketViewSlot.getSlotIndex()));

                    openRecipeSelectPopup(basketViewSlot.getSlotIndex());
                }
            });

            basketViewList.add(basketView);
        }



        // 흔들기 모션 옵션 버튼 정의 =====================================================
        len = SHAKING_OPTION_VIEW_ID_LIST.length;
        shakingOptionViewList        = new ArrayList<ShakingOptionView>();
        ShakingOptionView shakingOptionView;

        for(i = 0; i < len; i++){

            shakingOptionView = (ShakingOptionView)findViewById(SHAKING_OPTION_VIEW_ID_LIST[i]);
            shakingOptionView.setShakingOptionBtnCallback(shakingOptionBtnCallback);
            shakingOptionView.setOnOffUI(ShakingOptionView.STATE_OFF);
            shakingOptionViewList.add(shakingOptionView);
        }

        deoilSlider         = (IndicatorSeekBar)findViewById(R.id.deoilSeekBar);

        endTimeTxt          = (TextView)findViewById(R.id.endTimeTxt);


        recipeTimeMinuteInputTxt.setText("3");
        recipeTimeSecondInputTxt.setText("00");
    }

    private void initService(){

        //서비스 구동
        Intent serviceIntent = new Intent(this, MainService.class);
        bindService(serviceIntent, serviceConnection, Context.BIND_AUTO_CREATE);
    }

    private ShakingOptionBtnCallback shakingOptionBtnCallback = new ShakingOptionBtnCallback() {
        @Override
        public void callback(int $slotIndex, int $cmd, int $value) {

            switch($cmd){

                //슬롯 on / off 버튼 클릭
                case ShakingOptionBtnCallback.EVENT_OPTION_ONOFF:

                    updateShakingOptionState($slotIndex, $value);
                    break;

                //슬롯 슬라이더 작동
                case ShakingOptionBtnCallback.EVENT_OPTION_SLIDER:

                    updateShakingPointerUI($slotIndex);
                    break;

                //슬롯 -/+ 버튼 클릭
                case ShakingOptionBtnCallback.EVENT_OPTION_PLUS_MINUS:

                    updateShakingTimePoint($slotIndex, $value);
                    break;
            }
        }
    };

    private void selectRecipeToBasket(int $slotIndex, int $recipeIndex){

        basketViewList.get($slotIndex).setRecipeIndex($recipeIndex);
        mainService.writeMultiModbusData(ModbusData.ADDRESS_BASKET1_RECIPE_REGISTER + $slotIndex, new int[]{$recipeIndex+1});
        mainService.writeMultiModbusData(ModbusData.ADDRESS_BASKET1_RECIPE_CHANGE + $slotIndex, new int[]{1});
    }

    /**
     * 타겟 리스트 인덱스의 레시피 정보 불러오기
     * @param $index
     */
    private void loadRecipeData(int $index){

        RecipeData recipeData = MainApplication.mainData.getRecipeDataList().get($index);

        recipeNameInputTxt.setText(recipeData.getRecipeName());

        recipeTotalTime = recipeData.getTotalTime();

        int recipeTotalTimeMin = (int)(recipeTotalTime / 60);
        int recipeTotalTimeSec = recipeTotalTime % 60;

        if(recipeTotalTimeMin > 0)
            recipeTimeMinuteInputTxt.setText(String.valueOf(recipeTotalTimeMin));
        else
            recipeTimeMinuteInputTxt.setText("0");

        if(recipeTotalTimeSec > 0)
            recipeTimeSecondInputTxt.setText(String.valueOf(recipeTotalTimeSec));
        else
            recipeTimeSecondInputTxt.setText("0");

        if(recipeData.isShakingMotion1Use()){

            shakingOptionViewList.get(0).setOnOffUI(ShakingOptionView.STATE_ON);
            shakingOptionViewList.get(0).setShakingCount(recipeData.getShakingMotion1Count());
            shakingOptionViewList.get(0).setStartingTime(recipeData.getShakingMotion1StartTime());

            step1PointUI.setVisibility(View.VISIBLE);
            step1PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeData.getShakingMotion1StartTime() / recipeTotalTime - step1PointUI.getWidth() * 0.5f);
            updateShakingPointerUI(0);

        }else{

            shakingOptionViewList.get(0).setOnOffUI(ShakingOptionView.STATE_OFF);
            step1PointUI.setVisibility(View.INVISIBLE);
        }

        if(recipeData.isShakingMotion2Use()){

            shakingOptionViewList.get(1).setOnOffUI(ShakingOptionView.STATE_ON);
            shakingOptionViewList.get(1).setShakingCount(recipeData.getShakingMotion2Count());
            shakingOptionViewList.get(1).setStartingTime(recipeData.getShakingMotion2StartTime());

            step2PointUI.setVisibility(View.VISIBLE);
            step2PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeData.getShakingMotion2StartTime() / recipeTotalTime - step2PointUI.getWidth() * 0.5f);
            updateShakingPointerUI(1);

        }else{

            shakingOptionViewList.get(1).setOnOffUI(ShakingOptionView.STATE_OFF);
            step2PointUI.setVisibility(View.INVISIBLE);
        }

        if(recipeData.isShakingMotion3Use()){

            shakingOptionViewList.get(2).setOnOffUI(ShakingOptionView.STATE_ON);
            shakingOptionViewList.get(2).setShakingCount(recipeData.getShakingMotion3Count());
            shakingOptionViewList.get(2).setStartingTime(recipeData.getShakingMotion3StartTime());

            step3PointUI.setVisibility(View.VISIBLE);
            step3PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeData.getShakingMotion3StartTime() / recipeTotalTime - step3PointUI.getWidth() * 0.5f);
            updateShakingPointerUI(2);

        }else{

            shakingOptionViewList.get(2).setOnOffUI(ShakingOptionView.STATE_OFF);
            step3PointUI.setVisibility(View.INVISIBLE);
        }

        deoilSlider.setProgress(recipeData.getDeoilMotionCount());

        Util.showLongToast(activity, activity.getResources().getString(R.string.complete_load_data_msg));
    }
    
    /**
     * 타겟 리스트 인덱스에 작성된 레시피 정보 저장
     * @param $index
     */
    private void saveRecipeData(int $index){


        RecipeData recipeData = MainApplication.mainData.getRecipeDataList().get($index);

        recipeData.setValid(true);
        recipeData.setRecipeName(recipeNameInputTxt.getText().toString());
        recipeData.setTotalTime(recipeTotalTime);

        recipeData.setShakingMotion1Count(shakingOptionViewList.get(0).getShakingCount());
        recipeData.setShakingMotion1StartTime(shakingOptionViewList.get(0).getStartingTime());
        recipeData.setShakingMotion1Use((shakingOptionViewList.get(0).getOnOffState() == ShakingOptionView.STATE_ON)? true : false);

        recipeData.setShakingMotion2Count(shakingOptionViewList.get(1).getShakingCount());
        recipeData.setShakingMotion2StartTime(shakingOptionViewList.get(1).getStartingTime());
        recipeData.setShakingMotion2Use((shakingOptionViewList.get(1).getOnOffState() == ShakingOptionView.STATE_ON)? true : false);

        recipeData.setShakingMotion3Count(shakingOptionViewList.get(2).getShakingCount());
        recipeData.setShakingMotion3StartTime(shakingOptionViewList.get(2).getStartingTime());
        recipeData.setShakingMotion3Use((shakingOptionViewList.get(2).getOnOffState() == ShakingOptionView.STATE_ON)? true : false);

        recipeData.setDeoilMotionCount(deoilSlider.getProgress());

        Util.writeRecipeFile(activity);
        //완료 메세지 출력
        Util.showLongToast(activity, activity.getResources().getString(R.string.complete_save_data_msg));

        //저장된 레시피 정보 서버에 전송
        sendTargetData($index);
    }

    private boolean checkValidRecipeData(){

        if(recipeNameInputTxt.getText().toString().equals("")) {

            Util.showLongToast(activity, activity.getResources().getString(R.string.no_recipe_name));
            return false;

        }else if(recipeTotalTime < 1){

            Util.showLongToast(activity, activity.getResources().getString(R.string.no_recipe_time));
            return false;

        }else if(shakingOptionViewList.get(0).getOnOffState() == ShakingOptionView.STATE_ON
            && shakingOptionViewList.get(1).getOnOffState() == ShakingOptionView.STATE_ON
            && shakingOptionViewList.get(1).getStartingTime() - shakingOptionViewList.get(0).getStartingTime() < 60){

            Util.showLongToast(activity, activity.getResources().getString(R.string.not_enough_time_gap_motion_1_n_2));
            return false;

        }else if(shakingOptionViewList.get(1).getOnOffState() == ShakingOptionView.STATE_ON
                && shakingOptionViewList.get(2).getOnOffState() == ShakingOptionView.STATE_ON
                && shakingOptionViewList.get(2).getStartingTime() - shakingOptionViewList.get(1).getStartingTime() < 60){

            Util.showLongToast(activity, activity.getResources().getString(R.string.not_enough_time_gap_motion_2_n_3));
            return false;
        }


        return true;
    }

    /**
     * 타겟 포인터의 시간값 변경
     * @param $slotIndex
     * @param $value
     */
    private void updateShakingTimePoint(int $slotIndex, int $value){
        
        switch($slotIndex){

            case 0://첫번째

                int recipeStep1Time = shakingOptionViewList.get(0).getStartingTime() + $value;

                //첫번째 포인터 시간은 0보다 작을 수 없다.
                if(recipeStep1Time < 0){

                    return;
                }

                //첫번째 포인터 시간은 활성화된 두번째 포인터 시간을 초과할 수 없다.
                if(shakingOptionViewList.get(1).getOnOffState() == ShakingOptionView.STATE_ON
                    && recipeStep1Time >= shakingOptionViewList.get(1).getStartingTime() - 5){

                    return;
                }

                step1PointUI.setVisibility(View.VISIBLE);
                step1PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep1Time / recipeTotalTime - step1PointUI.getWidth() * 0.5f);
                shakingOptionViewList.get(0).setStartingTime( recipeStep1Time);
                updateShakingPointerUI(0);
                break;

            case 1://두번째

                int recipeStep2Time = shakingOptionViewList.get(1).getStartingTime() + $value;

                //두번째 포인터 시간은 활성화된 세번째 포인터 시간을 초과할 수 없다.
                if(shakingOptionViewList.get(2).getOnOffState() == ShakingOptionView.STATE_ON
                        && recipeStep2Time >= shakingOptionViewList.get(2).getStartingTime() - 5){

                    return;
                }

                //두번째 포인터 시간은 활성화된 첫번째 포인터 시간을 초과할 수 없다.
                if(shakingOptionViewList.get(0).getOnOffState() == ShakingOptionView.STATE_ON
                        && recipeStep2Time <= shakingOptionViewList.get(0).getStartingTime() + 5){

                    return;
                }

                step2PointUI.setVisibility(View.VISIBLE);
                step2PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep2Time / recipeTotalTime - step2PointUI.getWidth() * 0.5f);
                shakingOptionViewList.get(1).setStartingTime( recipeStep2Time);
                updateShakingPointerUI(1);
                break;

            case 2://세번째

                int recipeStep3Time = shakingOptionViewList.get(2).getStartingTime() + $value;

                //세번째 포인터 시간은 전체 조리시간을 초과할 수 없다.
                if(recipeStep3Time > recipeTotalTime){

                    return;
                }

                //세번째 포인터 시간은 활성화된 두번째 포인터 시간을 초과할 수 없다.
                if(shakingOptionViewList.get(1).getOnOffState() == ShakingOptionView.STATE_ON
                        && recipeStep3Time <= shakingOptionViewList.get(1).getStartingTime() + 5){

                    return;
                }

                step3PointUI.setVisibility(View.VISIBLE);
                step3PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep3Time / recipeTotalTime - step3PointUI.getWidth() * 0.5f);
                shakingOptionViewList.get(2).setStartingTime( recipeStep3Time);
                updateShakingPointerUI(2);
                break;
        }
    }

    /**
     * 타겟 포인터의 흔들기 횟수 변경
     * @param $slotIndex
     */
    private void updateShakingPointerUI(int $slotIndex){

        int startingTime;

        switch($slotIndex) {

            case 0://첫번째 옵션 슬롯

                startingTime = shakingOptionViewList.get(0).getStartingTime();

                int step1TimeMin = (int) (startingTime / 60);
                int step1TimeSec = startingTime % 60;

                step1PointInfoTxt.setText(getResources().getString(R.string.point_1st_title) + "\n" + Util.digit(step1TimeMin) + ":" + Util.digit(step1TimeSec) + "\n[" + String.valueOf(shakingOptionViewList.get(0).getShakingCount()) + "회]");
                break;

            case 1://두번째 옵션 슬롯

                startingTime = shakingOptionViewList.get(1).getStartingTime();

                int step2TimeMin = (int) (startingTime / 60);
                int step2TimeSec = startingTime % 60;

                step2PointInfoTxt.setText(getResources().getString(R.string.point_2nd_title) + "\n" + Util.digit(step2TimeMin) + ":" + Util.digit(step2TimeSec) + "\n[" + String.valueOf(shakingOptionViewList.get(1).getShakingCount()) + "회]");
                break;

            case 2://세번째 옵션 슬롯

                startingTime = shakingOptionViewList.get(2).getStartingTime();

                int step3TimeMin = (int) (startingTime / 60);
                int step3TimeSec = startingTime % 60;

                step3PointInfoTxt.setText(getResources().getString(R.string.point_3th_title) + "\n" + Util.digit(step3TimeMin) + ":" + Util.digit(step3TimeSec) + "\n[" + String.valueOf(shakingOptionViewList.get(2).getShakingCount()) + "회]");
                break;
        }
    }

    private void updateShakingOptionState(int $slotIndex, int $onOff){

        switch($slotIndex){

            case 0://첫번째 옵션 슬롯

                switch($onOff) {

                    case ShakingOptionView.STATE_OFF:

                        //첫번째 아이콘 off
                        step1PointUI.setVisibility(View.INVISIBLE);

                        //두번째 슬롯 및 포인터 같이 off
                        shakingOptionViewList.get(1).setOnOffUI(ShakingOptionView.STATE_OFF);
                        step2PointUI.setVisibility(View.INVISIBLE);

                        //세번째 슬롯 및 포인터 같이 off
                        shakingOptionViewList.get(2).setOnOffUI(ShakingOptionView.STATE_OFF);
                        step3PointUI.setVisibility(View.INVISIBLE);
                        break;

                    case ShakingOptionView.STATE_ON:

                        //조리 시간 미입력시 return.
                        if (recipeTotalTime == 0) return;

                        //첫번째 포인터 On
                        step1PointUI.setVisibility(View.VISIBLE);
                        int recipeStep1Time = (int) (recipeTotalTime * .5f);
                        step1PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep1Time / recipeTotalTime - step1PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(0).setStartingTime( recipeStep1Time);
                        updateShakingPointerUI(0);
                        break;
                }
                break;

            case 1://두번째

                switch($onOff) {

                    case ShakingOptionView.STATE_OFF:

                        //두번째 포인터 off
                        step2PointUI.setVisibility(View.INVISIBLE);

                        //세번째 슬롯 및 포인터 같이 off
                        shakingOptionViewList.get(2).setOnOffUI(ShakingOptionView.STATE_OFF);
                        step3PointUI.setVisibility(View.INVISIBLE);
                        break;

                    case ShakingOptionView.STATE_ON:

                        //첫번재 욥션 항목 on
                        shakingOptionViewList.get(0).setOnOffUI(ShakingOptionView.STATE_ON);

                        //조리 시간 미입력시 return.
                        if (recipeTotalTime == 0) return;

                        //첫번째 포인터 On
                        step1PointUI.setVisibility(View.VISIBLE);
                        int recipeStep1Time = (int) (recipeTotalTime * .33f);
                        step1PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep1Time / recipeTotalTime - step1PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(0).setStartingTime( recipeStep1Time);
                        updateShakingPointerUI(0);

                        //두번재 포인터 on
                        step2PointUI.setVisibility(View.VISIBLE);
                        int recipeStep2Time = (int) (recipeTotalTime * .66f);
                        step2PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep2Time / recipeTotalTime - step2PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(1).setStartingTime( recipeStep2Time);
                        updateShakingPointerUI(1);
                        break;
                }
                break;

            case 2://세번째

                switch($onOff) {

                    case ShakingOptionView.STATE_OFF:

                        //세번째 아이콘 off
                        step3PointUI.setVisibility(View.INVISIBLE);
                        break;

                    case ShakingOptionView.STATE_ON:

                        //첫번째 옵션 항목 on
                        shakingOptionViewList.get(0).setOnOffUI(ShakingOptionView.STATE_ON);
                        //두번째 옵션 항목 on
                        shakingOptionViewList.get(1).setOnOffUI(ShakingOptionView.STATE_ON);

                        //조리 시간 미입력시 return.
                        if (recipeTotalTime == 0) return;

                        //첫번째 포인터 On
                        step1PointUI.setVisibility(View.VISIBLE);
                        int recipeStep1Time = (int) (recipeTotalTime * .25f);
                        step1PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep1Time / recipeTotalTime - step1PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(0).setStartingTime( recipeStep1Time);
                        updateShakingPointerUI(0);

                        //두번째 포인터 On
                        step2PointUI.setVisibility(View.VISIBLE);
                        int recipeStep2Time = (int) (recipeTotalTime * .5f);
                        step2PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep2Time / recipeTotalTime - step2PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(1).setStartingTime( recipeStep2Time);
                        updateShakingPointerUI(1);

                        //세번째 포인터 On
                        step3PointUI.setVisibility(View.VISIBLE);
                        int recipeStep3Time = (int) (recipeTotalTime * .75f);
                        step3PointUI.setX(scheduleBarPosX + scheduleBarWidth * recipeStep3Time / recipeTotalTime - step3PointUI.getWidth() * 0.5f);
                        shakingOptionViewList.get(2).setStartingTime( recipeStep3Time);
                        updateShakingPointerUI(2);
                        break;
                }
                break;
        }
    }

    /**
     * 조리시간(분/초) 입력에따라 실시간으로 레시피 구성에 적용
     */
    private void updateRecipeTimeUI(){

        int min, sec;

        if(recipeTimeMinuteInputTxt.getText().toString().equals(""))
            min = 0;
        else
            min = Integer.parseInt(recipeTimeMinuteInputTxt.getText().toString());

        if(recipeTimeSecondInputTxt.getText().toString().equals(""))
            sec = 0;
        else
            sec = Integer.parseInt(recipeTimeSecondInputTxt.getText().toString());

        recipeTotalTime = min * 60 + sec;

        endTimeTxt.setText(Util.digit(min) + ":" + Util.digit(sec));
    }

    public void onBtnClick(View view) {

        switch (view.getId()) {

            case R.id.tutorialMenuBtn:
            case R.id.cookingMenuBtn:
            case R.id.recipeMenuBtn:

                selectMenu(view.getId());
                break;

            case R.id.settingMenuBtn:

                directTeachingBtnStatePrev  = -1;
                gripperBtnStatePrev         = -1;
                programBtnStatePrev         = -1;

                selectMenu(view.getId());
                break;

            case R.id.recipeSaveBtn:

                //양식 검사
                if(checkValidRecipeData() == false)
                    return;

                openRecipeSavePopup();
                break;

            case R.id.recipeLoadBtn:

                openRecipeLoadPopup();
                break;

            case R.id.recipeNewBtn:

                initRecipeEditUI();
                break;

            case R.id.directTeachingOnBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DIRECT_MODE_CMD, new int[]{1});
                break;

            case R.id.directTeachingOffBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DIRECT_MODE_CMD, new int[]{2});
                break;

            case R.id.gripperOnBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_GRIPPER_MODE_CMD, new int[]{1});
                break;

            case R.id.gripperOffBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_GRIPPER_MODE_CMD, new int[]{2});
                break;

            case R.id.resetBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_RECOVERY_CMD, new int[]{1});
                break;

            case R.id.collisionResetBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_RESET_COLLISION_CMD, new int[]{1});
                break;

            case R.id.playProgramBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DEFAULT_PROGRAM_CMD, new int[]{1});
                break;

            case R.id.pauseProgramBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DEFAULT_PROGRAM_CMD, new int[]{3});
                break;

            case R.id.resumeProgramBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DEFAULT_PROGRAM_CMD, new int[]{2});
                break;

            case R.id.stopProgramBtn:

                mainService.writeMultiModbusData(ModbusData.ADDRESS_DEFAULT_PROGRAM_CMD, new int[]{4});
                break;

//            case R.id.moveToHomePosBtn:
//
//                break;
//
//            case R.id.moveToZeroPosBtn:
//
//                break;
//
//            case R.id.moveToPackagePosBtn:
//
//                break;

            case R.id.setRobotIPBtn:

                String ipAddr = ipInputTxt.getText().toString();

                SharedPrefManager.getInstance(activity).setRobotIP(ipAddr);
                MainApplication.mainData.setRobotIp(ipAddr);
                ipAddressTxt.setText(getResources().getString(R.string.header_ip_label) + " " + ipAddr);
                break;

            case R.id.uploadRecipeBtn:

                sendRecipeDataList();
                Util.showLongToast(activity, getResources().getString(R.string.complete_to_upload_recipe_data));
                break;
        }
    }//func

    private void selectStep1TimeOption(int $index){

    }

    private void selectMenu(int $btnId){

        focusMenuBtn($btnId);
        openMenuUI($btnId);
    }

    private void focusMenuBtn(int $btnId){

        int len = menuBtnList.size();
        TextView btn;

        for(int i = 0; i < len; i++){

            btn = menuBtnList.get(i);
            if(btn.getId() == $btnId){

                btn.setBackground(ContextCompat.getDrawable(this, R.drawable.menu_btn_bg));
                btn.setTextColor(getResources().getColor(R.color.blue, this.getTheme()));

            }else{

                btn.setBackground(null);
                btn.setTextColor(getResources().getColor(R.color.t_g100, this.getTheme()));
            }

        }
    }//func

    private void openMenuUI(int $btnId) {

        closeKeyboard();

        int len = menuUIList.size();
        for (int i = 0; i < len; i++)
            menuUIList.get(i).setVisibility(View.INVISIBLE);

        switch ($btnId){

            case R.id.tutorialMenuBtn:
                tutorialMenuUI.setVisibility(View.VISIBLE);
                imageSlider.setCurrentPagePosition(0);
                break;
            case R.id.cookingMenuBtn:      workMenuUI.setVisibility(View.VISIBLE);  break;
            case R.id.recipeMenuBtn:    recipeMenuUI.setVisibility(View.VISIBLE);   break;
            case R.id.settingMenuBtn:   settingMenuUI.setVisibility(View.VISIBLE);  break;
        }
    }

    /**
     * 레시피 편집 화면 초기화하기
     */
    private void initRecipeEditUI(){

        int len, i;

        recipeNameInputTxt.setText("");

        recipeTimeMinuteInputTxt.setText("3");
        recipeTimeSecondInputTxt.setText("00");

        len = shakingOptionViewList.size();
        for(i = 0; i < len; i++) {

            shakingOptionViewList.get(i).initSetting();
            shakingOptionViewList.get(i).setOnOffUI(ShakingOptionView.STATE_OFF);
        }

        deoilSlider.setProgress(1);

        step1PointUI.setVisibility(View.INVISIBLE);
        step2PointUI.setVisibility(View.INVISIBLE);
        step3PointUI.setVisibility(View.INVISIBLE);

        Util.showShortToast(activity, activity.getResources().getString(R.string.init_recipe_msg));
    }

    /**
     * '레시피 저장하기 팝업' 생성
     */
    private void openRecipeSavePopup(){

        Intent intent = new Intent(this, RecipeListPopup.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
        intent.putExtra(Config.POPUP_ID, Config.POPUP_ID_RECIPE_SAVE);

        popupLauncher.launch(intent);
        overridePendingTransition(0,0);
    }

    /**
     * '레시피 불러오기 팝업' 생성
     */
    private void openRecipeLoadPopup(){

        Intent intent = new Intent(this, RecipeListPopup.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
        intent.putExtra(Config.POPUP_ID, Config.POPUP_ID_RECIPE_LOAD);

        popupLauncher.launch(intent);
        overridePendingTransition(0,0);
    }

    /**
     * '레시피 선택하기 팝업' 생성
     */
    private void openRecipeSelectPopup(int $slotIndex){

        Intent intent = new Intent(this, RecipeListPopup.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
        intent.putExtra(Config.POPUP_ID, Config.POPUP_ID_RECIPE_SELECT);
        intent.putExtra(Config.RECIPE_POPUP_INTENT_SLOT_INDEX, $slotIndex);

        popupLauncher.launch(intent);
        overridePendingTransition(0,0);
    }

    /**
     * Fryer 조리 완료 yes/no 팝업 생성
     */
    private void openCookingYesNoPopup(int $slotIndex){

        YesNoPopupDialog yesNoPopupDialog = new YesNoPopupDialog(
                activity,
                Util.getString(activity, R.string.ask_fin_cooking_msg),
                new YesNoDialogListener() {
                    @Override
                    public void onClickYes() {

                        mainService.writeMultiModbusData(ModbusData.ADDRESS_TERMINATE_COOKING_CMD + $slotIndex, new int[]{1});
                    }
                });

        yesNoPopupDialog.setCanceledOnTouchOutside(false);
        yesNoPopupDialog.setCancelable(false);
        yesNoPopupDialog.show();
    }



    ServiceConnection serviceConnection = new ServiceConnection() {

        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {

            NRMKLog.log("onServiceConnected");

            MainService.ServiceBinder serviceBinder = (MainService.ServiceBinder)service;
            mainService = serviceBinder.getService();
            mainService.registerCallback(serviceCallback);

            mainService.startStateTimer();
        }

        @Override
        public void onServiceDisconnected(ComponentName name) {

            NRMKLog.log("onServiceDisconnected");
        }
    };

    MainService.ServiceCallback serviceCallback = new MainService.ServiceCallback() {

        @Override
        public void updateRealTimeData(ModbusData $modbusData) {

            int len = $modbusData.getDataList().length;
//            String data = "";
//
//            for(int i = 0; i < len; i++)
//                data = data + $modbusData.getDataList()[i] + ",";
//
//            NRMKLog.log("realtime data : " + data);

            switch($modbusData.getStartAddress()){

                case ModbusData.ADDRESS_REALTIME_STATE:

                    updateUI($modbusData.getDataList());
                    break;

                case ModbusData.ADDRESS_SETTING_BTN_STATE:
                    NRMKLog.log("==> " + Arrays.toString($modbusData.getDataList()));
                    updateSettingUI($modbusData.getDataList());
                    break;

            }


        }

        @Override
        public void sendRecipe() {

            sendRecipeDataList();
        }

        @Override
        public void connectionFailed() {

            ipAddressTxt.setTextColor(getResources().getColor(R.color.red, activity.getTheme()));
            robotStateTxt.setText(getResources().getString(R.string.header_robot_state_label) + " - ");
            runningTimeTxt.setText(getResources().getString(R.string.header_work_time_label) + " - ");
            workCountTxt.setText(getResources().getString(R.string.header_work_count_label) + " - ");
            workStateTxt.setText(getResources().getString(R.string.header_work_state_label) + " - ");
        }

        @Override
        public void writeFailed() {

            Util.showLongToast(activity, getResources().getString(R.string.failed_to_send_data));
        }

    };

    private void sendRecipeDataList(){

        NRMKLog.log("======================== sendRecipData ========================");

        int len = MainApplication.mainData.getRecipeDataList().size();

        for(int i = 0; i < len; i++)
            sendTargetData(i);
    }

    private void sendTargetData(int $recipeIndex){

        int startingAddress = ModbusData.ADDRESS_UPLOAD_RECIPE;
        int dataLen = 15;
        int[] data;

        RecipeData recipeData = MainApplication.mainData.getRecipeDataList().get($recipeIndex);

        data    = new int[dataLen];
        data[0] = (recipeData.isValid() == true)? (int)(recipeData.getTotalTime() / 60) : 0;
        data[1] = (recipeData.isValid() == true)? (int)(recipeData.getTotalTime() % 60) : 0;

        data[2] = (recipeData.isShakingMotion1Use() == true)? 1 : 0;
        data[3] = recipeData.getShakingMotion1Count();
        data[4] = (int)(recipeData.getShakingMotion1StartTime() / 60);
        data[5] = (int)(recipeData.getShakingMotion1StartTime() % 60);

        data[6] = (recipeData.isShakingMotion2Use() == true)? 1 : 0;
        data[7] = recipeData.getShakingMotion2Count();
        data[8] = (int)(recipeData.getShakingMotion2StartTime() / 60);
        data[9] = (int)(recipeData.getShakingMotion2StartTime() % 60);

        data[10] = (recipeData.isShakingMotion3Use() == true)? 1 : 0;
        data[11] = recipeData.getShakingMotion3Count();
        data[12] = (int)(recipeData.getShakingMotion3StartTime() / 60);
        data[13] = (int)(recipeData.getShakingMotion3StartTime() % 60);

        data[14] = recipeData.getDeoilMotionCount();

//        NRMKLog.log(Arrays.toString(data));
        mainService.writeMultiModbusData(startingAddress + $recipeIndex * dataLen, data);
    }

    private void updateSettingUI(int[] $dataList){

        if(settingMenuUI.getVisibility() == View.VISIBLE){

            int directTeachingBtnState  = $dataList[0];
            int gripperBtnState         = $dataList[1];
            int programBtnState         = $dataList[2];

            if(directTeachingBtnStatePrev != directTeachingBtnState) {

                directTeachingOnBtn.setPressed(false);
                directTeachingOffBtn.setPressed(false);

                switch (directTeachingBtnState) {

                    case 1://on

                        directTeachingOnBtn.setPressed(true);
                        break;

                    case 2://off

                        directTeachingOffBtn.setPressed(true);
                        break;
                }
                directTeachingBtnStatePrev = directTeachingBtnState;
            }//


            if(gripperBtnStatePrev != gripperBtnState) {

                gripperOnBtn.setPressed(false);
                gripperOffBtn.setPressed(false);

                switch (gripperBtnState) {

                    case 0://init
                        break;

                    case 1://on

                        gripperOnBtn.setPressed(true);
                        break;

                    case 2://off

                        gripperOffBtn.setPressed(true);
                        break;
                }
                gripperBtnStatePrev = directTeachingBtnState;
            }


            if(programBtnStatePrev != programBtnState) {

                playBtn.setPressed(false);
                pauseBtn.setPressed(false);
                stopBtn.setPressed(false);
                resumeBtn.setPressed(false);

                switch (programBtnState) {

                    case 0://init
                        break;

                    case 1://play

                        playBtn.setPressed(true);
                        break;

                    case 2://resume

                        resumeBtn.setPressed(true);
                        break;

                    case 3://pause

                        pauseBtn.setPressed(true);
                        break;

                    case 4://stop

                        stopBtn.setPressed(true);
                        break;
                }
                programBtnStatePrev = programBtnState;
            }//
        }
    }

    private void updateUI(int[] $dataList){

        int len, i;

        ipAddressTxt.setTextColor(getResources().getColor(R.color.light_green, activity.getTheme()));
        robotStateTxt.setText(getResources().getString(R.string.header_robot_state_label) + " " + Config.ROBOT_STATE[$dataList[1]]);
        runningTimeTxt.setText(getResources().getString(R.string.header_work_time_label) + " " + String.valueOf($dataList[2]) + "시간 " + String.valueOf($dataList[3]) + "분");
        workCountTxt.setText(getResources().getString(R.string.header_work_count_label) + " " + String.valueOf($dataList[4]));
        workStateTxt.setText(getResources().getString(R.string.header_work_state_label) + " " + Config.WORK_STATE[$dataList[5]]);

        //실행 메뉴 사용중인 경우, 관련 상태 업데이트
        if(workMenuUI.getVisibility() == View.VISIBLE){

            len = fryerViewList.size();
            for(i = 0 ; i < len; i++)
                fryerViewList.get(i).updateInfo(
                        $dataList[ModbusData.ADDRESS_FRYER1_STATE + i],
                        $dataList[ModbusData.ADDRESS_FRYER1_PROGRESS_TIME_MIN + i],
                        $dataList[ModbusData.ADDRESS_FRYER1_PROGRESS_TIME_SEC + i]);

            len = basketViewList.size();
            for(i = 0 ; i < len; i++)
                basketViewList.get(i).updateInfo(
                        $dataList[ModbusData.ADDRESS_BASKET1_STATE + i],
                        $dataList[ModbusData.ADDRESS_BASKET1_RECIPE_REGISTER + i]);
        }

//        NRMKLog.log("received : " + Arrays.toString($dataList));
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event)
    {
        if ((keyCode == KeyEvent.KEYCODE_BACK))
        {
            //back버튼 입력으로인한, 의도치 않은 뒤로가기/앱 종료를 방지
            return false;
        }
        return super.onKeyDown(keyCode, event);
    }

    private void closeKeyboard(){

        if(this.getCurrentFocus() != null) {

            InputMethodManager inputMethodManager = (InputMethodManager) this.getSystemService(Activity.INPUT_METHOD_SERVICE);
            inputMethodManager.hideSoftInputFromWindow(this.getCurrentFocus().getWindowToken(), 0);
        }
    }
}