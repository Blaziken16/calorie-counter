package com.blaziken.caloriecounter.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.blaziken.caloriecounter.screens.temp.Plan

@Composable
fun personalizationScreen(modifier: Modifier){
    val plans = listOf(
        Plan("maintain", "Maintain","2000 Kcal"),
        Plan("gain", "Gain","2500 Kcal"),
        Plan("cut", "Cut","1500 Kcal")
    )
    var selectedPlan by remember { mutableStateOf<String>("maintain") }
    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment =  Alignment.CenterHorizontally,
    ) {
        Text(
            text = "Select your Plan",
            fontSize = 20.sp,
            fontWeight = FontWeight.Bold
        )
        Spacer(Modifier.height(50.dp))
            plans.forEach{ plan ->
                selectablePlanCard(
                    plan = plan,
                    isSelected = selectedPlan == plan.id,
                    onClick = {
                        selectedPlan = plan.id
                    }
                )
                Spacer(Modifier.height(26.dp))
            }
            val selected = plans.first { it.id == selectedPlan }
            Text("Selected: ${selected.title}")
        Spacer(Modifier.height(26.dp))
        Button(
            onClick = {/*TODO*/}
        ) { Text("Continue") }
    }
}

@Composable
fun selectablePlanCard(
    plan: Plan,
    isSelected: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
){
    val borderColor = if (isSelected) MaterialTheme.colorScheme.primary else Color.LightGray
    Card(
        onClick = onClick,
        modifier = modifier.height(120.dp),
        shape = RoundedCornerShape(14.dp),
        border = BorderStroke(
            width = if(isSelected) 2.dp else 1.dp,
            color = borderColor
        )
    ) {
        Column(
            modifier = Modifier.fillMaxSize().padding(8.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(plan.title, fontSize = 18.sp, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(4.dp))
            Text(plan.description, fontSize = 13.sp)
        }
    }
}