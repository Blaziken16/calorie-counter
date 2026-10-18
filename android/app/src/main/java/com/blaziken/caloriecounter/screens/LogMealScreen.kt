package com.blaziken.caloriecounter.screens

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp

@Composable
fun LogMealScreen(){
    var foodName by remember { mutableStateOf("") }
    var calories by remember { mutableStateOf("") }
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.Center
    ) {
        OutlinedTextField(
            value = foodName,
            onValueChange = {
                foodName = it
            },
            label = {
                Text(text = "Name of your meal")
            }
        )
        OutlinedTextField(
            value = calories,
            onValueChange = {
                calories = it
            },
            label = {
                Text(text = "Calories")
            }
        )
    }
}

@Preview(showBackground = true)
@Composable
fun logMealPreview(){
    LogMealScreen()
}