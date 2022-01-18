package com.neuromeka.fryingtemplatapp.data;

import com.neuromeka.fryingtemplatapp.util.NRMKLog;

import org.json.JSONException;
import org.json.JSONObject;

public class RecipeData {

    private boolean isValid                     = false;
    private String recipeName                   = "";
    private int totalTime                       = 0;

    private boolean shakingMotion1Use           = false;
    private int shakingMotion1Count             = 1;
    private int shakingMotion1StartTime         = 0;

    private boolean shakingMotion2Use           = false;
    private int shakingMotion2Count             = 1;
    private int shakingMotion2StartTime         = 0;

    private boolean shakingMotion3Use           = false;
    private int shakingMotion3Count             = 1;
    private int shakingMotion3StartTime         = 0;

    private int deoilMotionCount                = 1;




    public void applyJson(JSONObject $jsonObj){

        try {

            isValid                 = $jsonObj.getBoolean("isValid");
            recipeName              = $jsonObj.getString("recipeName");
            totalTime               = $jsonObj.getInt("totalTime");

            shakingMotion1Use       = $jsonObj.getBoolean("shakingMotion1Use");
            shakingMotion1Count     = $jsonObj.getInt("shakingMotion1Count");
            shakingMotion1StartTime = $jsonObj.getInt("shakingMotion1StartTime");

            shakingMotion2Use       = $jsonObj.getBoolean("shakingMotion2Use");
            shakingMotion2Count     = $jsonObj.getInt("shakingMotion2Count");
            shakingMotion2StartTime = $jsonObj.getInt("shakingMotion2StartTime");

            shakingMotion3Use       = $jsonObj.getBoolean("shakingMotion3Use");
            shakingMotion3Count     = $jsonObj.getInt("shakingMotion3Count");
            shakingMotion3StartTime = $jsonObj.getInt("shakingMotion3StartTime");

            deoilMotionCount        = $jsonObj.getInt("deoilMotionCount");

        }catch (JSONException je){

            NRMKLog.log("[applyJson] parsing error : " + je.getMessage());
        }
    }

    public JSONObject convertToJSON(){

        JSONObject obj = new JSONObject();

        try {

            obj.put("isValid", isValid);
            obj.put("recipeName", recipeName);
            obj.put("totalTime", totalTime);

            obj.put("shakingMotion1Use", shakingMotion1Use);
            obj.put("shakingMotion1Count", shakingMotion1Count);
            obj.put("shakingMotion1StartTime", shakingMotion1StartTime);

            obj.put("shakingMotion2Use", shakingMotion2Use);
            obj.put("shakingMotion2Count", shakingMotion2Count);
            obj.put("shakingMotion2StartTime", shakingMotion2StartTime);

            obj.put("shakingMotion3Use", shakingMotion3Use);
            obj.put("shakingMotion3Count", shakingMotion3Count);
            obj.put("shakingMotion3StartTime", shakingMotion3StartTime);

            obj.put("deoilMotionCount", deoilMotionCount);

        }catch (JSONException je){

            je.printStackTrace();
        }

        return obj;
    }

    public boolean isValid() {
        return isValid;
    }

    public void setValid(boolean exist) {
        isValid = exist;
    }

    public String getRecipeName() {
        return recipeName;
    }

    public void setRecipeName(String recipeName) {
        this.recipeName = recipeName;
    }

    public int getTotalTime() {
        return totalTime;
    }

    public void setTotalTime(int totalTime) {
        this.totalTime = totalTime;
    }

    public boolean isShakingMotion1Use() {
        return shakingMotion1Use;
    }

    public void setShakingMotion1Use(boolean shakingMotion1Use) {
        this.shakingMotion1Use = shakingMotion1Use;
    }

    public int getShakingMotion1Count() {
        return shakingMotion1Count;
    }

    public void setShakingMotion1Count(int shakingMotion1Count) {
        this.shakingMotion1Count = shakingMotion1Count;
    }

    public int getShakingMotion1StartTime() {
        return shakingMotion1StartTime;
    }

    public void setShakingMotion1StartTime(int shakingMotion1StartTime) {
        this.shakingMotion1StartTime = shakingMotion1StartTime;
    }

    public boolean isShakingMotion2Use() {
        return shakingMotion2Use;
    }

    public void setShakingMotion2Use(boolean shakingMotion2Use) {
        this.shakingMotion2Use = shakingMotion2Use;
    }

    public int getShakingMotion2Count() {
        return shakingMotion2Count;
    }

    public void setShakingMotion2Count(int shakingMotion2Count) {
        this.shakingMotion2Count = shakingMotion2Count;
    }

    public int getShakingMotion2StartTime() {
        return shakingMotion2StartTime;
    }

    public void setShakingMotion2StartTime(int shakingMotion2StartTime) {
        this.shakingMotion2StartTime = shakingMotion2StartTime;
    }

    public boolean isShakingMotion3Use() {
        return shakingMotion3Use;
    }

    public void setShakingMotion3Use(boolean shakingMotion3Use) {
        this.shakingMotion3Use = shakingMotion3Use;
    }

    public int getShakingMotion3Count() {
        return shakingMotion3Count;
    }

    public void setShakingMotion3Count(int shakingMotion3Count) {
        this.shakingMotion3Count = shakingMotion3Count;
    }

    public int getShakingMotion3StartTime() {
        return shakingMotion3StartTime;
    }

    public void setShakingMotion3StartTime(int shakingMotion3StartTime) {
        this.shakingMotion3StartTime = shakingMotion3StartTime;
    }

    public int getDeoilMotionCount() {
        return deoilMotionCount;
    }

    public void setDeoilMotionCount(int deoilMotionCount) {
        this.deoilMotionCount = deoilMotionCount;
    }
}
