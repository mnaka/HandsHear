#include <stdio.h>

double batteryLife(double measuredValue, double lastFullChargeOutput){
  double remainingPercentage = 0.0;
  remainingPercentage = measuredValue/lastFullChargeOutput;
  return remainingPercentage;
}

int discreteBatteryLife(double remainingPercentage){
  if (remainingPercentage > 0.5){
    // charging
    if (remainingPercentage > 1.0){
      return 5;
    }
    // full
    else if (remainingPercentage > 0.75){
      return 4;
    }
    // 3/4ths full
    else{
      return 3;
    }
  }
  else{
    //Warning
    if (remainingPercentage < 0.1){
      return 0;
    }
    //1/4th full
    else if (remainingPercentage < 0.25){
        return 1;
      }
    //half full
    else{
      return 2;
    }
  }
}
int main(){
  double measurement = batteryLife(3.5, 3.7);
  printf("Raw Measurement Value: %f\n", measurement);
  printf("Discrete Form: %i\n", discreteBatteryLife(measurement));
  return 0;
}
