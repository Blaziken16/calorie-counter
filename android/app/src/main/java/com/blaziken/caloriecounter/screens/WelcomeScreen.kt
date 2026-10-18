package com.blaziken.caloriecounter.screens

import androidx.compose.material3.Icon
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp


@Composable
fun welcomeScreen(modifier: Modifier){
    var AccountName by remember { mutableStateOf("") }
    var userHeight by remember { mutableStateOf("") }
    var userWeight by remember { mutableStateOf("") }

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
        Row(
            verticalAlignment = Alignment.CenterVertically
        ) {
            OutlinedTextField(
                modifier = Modifier.width(100.dp).height(60.dp),
                value= userWeight,
                onValueChange = {
                    userWeight = it
                },
                label = {Text(
                    text="Weight",
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                    style= MaterialTheme.typography.bodyMedium.copy(
                        fontSize = 14.sp
                    )
                )}
            )

            Spacer(modifier = Modifier.width(20.dp))

            OutlinedTextField(
                modifier = Modifier.width(100.dp).height(60.dp),
                value= userHeight,
                onValueChange = {
                    userHeight = it
                },
                label = {Text(
                    text="Height",
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                    style= MaterialTheme.typography.bodyMedium.copy(
                        fontSize = 14.sp
                    )
                )}
            )
        }

        Spacer(modifier = Modifier.height(20.dp))

        Button(onClick = {/*TODO*/}) {
            Text(text = "Continue")

        }
    }
}

@Preview(showBackground = true)
@Composable
fun welcomeScreenPreview(){
    welcomeScreen(modifier = Modifier)
}