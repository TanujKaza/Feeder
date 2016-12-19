package com.example.harsh.feeder01;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import static com.example.harsh.feeder01.MainActivity.MyPREFERENCES;

public class Logout extends AppCompatActivity {

    @Override
    public void onBackPressed(){}
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_logout);
        Context context=this.getApplicationContext();
        SharedPreferences sharedpreferences = context.getSharedPreferences(MyPREFERENCES, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedpreferences.edit();
        editor.putBoolean("LoggedIn",true);
        editor.commit();
    }
    public void logout(View view){
        SharedPreferences sharedpreferences = getSharedPreferences(MyPREFERENCES, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedpreferences.edit();
        editor.putBoolean("LoggedIn",false);
        editor.commit();
    }

    public void feedbackform(View view){
        Intent intent = new Intent(this,feedback.class);
        startActivity(intent);
    }
}
