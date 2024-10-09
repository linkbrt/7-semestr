package com.example.lr2

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.view.Menu
import android.view.MenuItem
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setTheme(R.style.AppTheme)
        setContentView(R.layout.activity_main)

        val hoursEditText = findViewById<EditText>(R.id.hoursEditText)
        val minutesEditText = findViewById<EditText>(R.id.minutesEditText)
        val resultTextView = findViewById<TextView>(R.id.resultTextView)
        val calculateButton = findViewById<Button>(R.id.calculateButton)

        calculateButton.setOnClickListener {
            val hours = hoursEditText.text.toString().toIntOrNull() ?: 0
            val minutes = minutesEditText.text.toString().toIntOrNull() ?: 0

           if (hours == 0 && minutes == 0){
               val toast = Toast.makeText(this, R.string.app_name, Toast.LENGTH_SHORT)
               val inflater = layoutInflater
               val vw = inflater.inflate(R.layout.toast, null)
               toast.view = vw
               toast.show()
               return@setOnClickListener
           }

            val totalSeconds = (hours * 60 + minutes) * 60


            resultTextView.text = "Введенное время в секундах: $totalSeconds"
        }
    }
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val id = item.itemId
        val infoTextView = findViewById<TextView>(R.id.resultTextView)

        val hoursEditText = findViewById<EditText>(R.id.hoursEditText)
        val minutesEditText = findViewById<EditText>(R.id.minutesEditText)
        var hours = hoursEditText.text.toString().toIntOrNull() ?: 0
        var minutes = minutesEditText.text.toString().toIntOrNull() ?: 0

        return when (id) {
            R.id.action_plushour -> {
                hours += 1
                hoursEditText.setText(hours.toString())
                true
            }

            R.id.action_minushour -> {
                if (hours < 1) {
                    hours = 0
                } else {
                    hours -= 1
                }
                hoursEditText.setText(hours.toString())
                true
            }

            R.id.action_plusminute -> {
                minutes += 1
                minutesEditText.setText(minutes.toString())
                true
            }

            R.id.action_minusminute -> {
                if (minutes < 1)  {
                    minutes = 0
                } else {
                    minutes -= 1
                }
                minutesEditText.setText(minutes.toString())
                true
            }

            else -> super.onOptionsItemSelected(item)
        }
    }
    }