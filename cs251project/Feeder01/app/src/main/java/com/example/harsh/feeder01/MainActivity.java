package com.example.harsh.feeder01;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.view.View;
import android.util.Log;
import org.json.JSONObject;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.net.URLEncoder;



import static android.R.attr.name;

public class MainActivity extends AppCompatActivity {
    public static final String MyPREFERENCES= "UserInfo";
    Intent intent;
    SharedPreferences sharedpreferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Context context=this.getApplicationContext();
        Intent intent = new Intent(this, Logout.class);
        sharedpreferences = context.getSharedPreferences(MyPREFERENCES, Context.MODE_PRIVATE);

        if(sharedpreferences.getBoolean("LoggedIn",false)){
            startActivity(intent);
        }
    }

    public static final String MY_PREFS_NAME = "UserData";
    public void login(View view) {
        if(view.getId()==R.id.lbutton){
            new SendPostRequest().execute();
            EditText imail = (EditText) findViewById(R.id.etext);
            EditText ipassword = (EditText) findViewById(R.id.ptext);
            String roll = imail.getText().toString();
            String password = ipassword.getText().toString();

            Context context=this.getApplicationContext();
            SharedPreferences userdata = context.getSharedPreferences(MY_PREFS_NAME, 0);
            SharedPreferences.Editor user_editor = userdata.edit();
            user_editor.putString("roll", roll);
            user_editor.apply();
        }

    }

    public class SendPostRequest extends AsyncTask<String, String, String> {
        EditText imail = (EditText) findViewById(R.id.etext);
        EditText ipassword = (EditText) findViewById(R.id.ptext);
        String roll = imail.getText().toString();
        String password = ipassword.getText().toString();

        protected void onPreExecute() {
        }

        protected String doInBackground(String... arg0) {
            try {
                String serverURL="http://10.0.2.2:8001/authenticate/";
                URL url = new URL(serverURL);
                JSONObject postDataParams = new JSONObject();
                postDataParams.put("roll_num", roll);
                postDataParams.put("password", password);

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
            if(result.equals("False"))
            {
                Toast.makeText(getApplicationContext(),"Invalid credentials",
                        Toast.LENGTH_LONG).show();
            }
            else
            if(result.equals("True"))
            {
                Intent intent2 = new Intent(MainActivity.this, Logout.class);
                startActivity(intent2);
            }
            else
            {
                Toast.makeText(getApplicationContext(),result,
                        Toast.LENGTH_LONG).show();
            }
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
};

