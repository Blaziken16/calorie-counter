package com.blaziken.caloriecounter.screens

import androidx.compose.material3.Icon
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp


@Composable
fun welcomeScreen(modifier: Modifier){
    var AccountName by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment =  Alignment.CenterHorizontally
    ) {
        Text(text= "Calorie-Counter")
        Spacer(modifier = Modifier.height(20.dp))

        OutlinedTextField(
            value= AccountName,
            onValueChange = {
            AccountName = it
            },
            label = {Text(text="Enter your Nick Name")}
        )

        Spacer(modifier = Modifier.height(20.dp))

        Button(onClick = {/*TODO*/}) {
            Text(text = "Continue")

        }
    }
}

