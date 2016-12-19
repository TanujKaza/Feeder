package com.example.harsh.feeder01;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.content.SharedPreferences;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RatingBar;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.Iterator;

import static com.example.harsh.feeder01.MainActivity.MY_PREFS_NAME;

public class feedback extends AppCompatActivity {
    public static String roll;
    public JSONObject data;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feedback);
        /*Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);*/

        /*FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });*/

       /* Context context=this.getApplicationContext();
        SharedPreferences userdata = context.getSharedPreferences(MY_PREFS_NAME, 0);
        roll  = userdata.getString("roll", "No name defined");*/

       new SendPostRequest().execute();



        RelativeLayout relativeLayout = (RelativeLayout) findViewById(R.id.feedback);

        LinearLayout ratings = new LinearLayout(this);
        ratings.setOrientation(LinearLayout.VERTICAL);
        for(int index = 0; index < 7; index++){
            RatingBar rating = new RatingBar(this);
            TextView question = new TextView(this);
            final TextView txtRatingValue = new TextView(this);
            question.setText("Feedback Question");
            question.setId(3*index);
            txtRatingValue.setId(3*index+1);
            rating.setId(3*index+2);
            ratings.addView(question);
            ratings.addView(rating);

            rating.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
                public void onRatingChanged(RatingBar ratingBar, float rating,
                                            boolean fromUser) {

                    txtRatingValue.setText(String.valueOf(rating));

                }
            });
        }
        relativeLayout.addView(ratings);
    }

    public class SendPostRequest extends AsyncTask<String, String, String> {
        protected void onPreExecute() {
        }

        protected String doInBackground(String... arg0) {
            try {
                String serverURL="http://10.0.2.2:8001/feedback/android";//authenticate/";
                URL url = new URL(serverURL);
                JSONObject postDataParams = new JSONObject();
                postDataParams.put("feedback_id", 66);
                Log.e("params", postDataParams.toString());
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");
                conn.setDoInput(true);
                conn.setDoOutput(true);
                OutputStream os = conn.getOutputStream();
                BufferedWriter writer = new BufferedWriter(
                        new OutputStreamWriter(os, "UTF-8"));
                writer.write(getPostDataString(postDataParams));

                writer.flush();
                writer.close();
                os.close();

                int responseCode=conn.getResponseCode();

                if (responseCode == HttpURLConnection.HTTP_OK) {
                    BufferedReader responsestream=new BufferedReader(new
                            InputStreamReader(
                            conn.getInputStream()));
                    StringBuffer sb = new StringBuffer("");
                    String line="";

                    while((line = responsestream.readLine()) != null) {
                        sb.append(line);
                    }
                    responsestream.close();
                    return sb.toString();
                }
                else {
                    return new String("false : "+responseCode);
                }
            }
            catch (Exception e) {
                return new String("Exception: " + e.getMessage());
            }
        }

        @Override
        protected void onPostExecute(String result) {
           /* try {
                data = new JSONObject(result);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            Log.i("answer", data.toString());*/
        }
    }
    public String getPostDataString(JSONObject params) throws Exception {

        StringBuilder result = new StringBuilder();
        boolean first = true;

        Iterator<String> itr = params.keys();

        while (itr.hasNext()) {

            String key = itr.next();
            Object value = params.get(key);

            if (first)
                first = false;
            else
                result.append("&");

            result.append(URLEncoder.encode(key, "UTF-8"));
            result.append("=");
            result.append(URLEncoder.encode(value.toString(), "UTF-8"));

        }
        return result.toString();
    }

}
