

export type DailyAvgTemperatureType = {
    date: string;
    avg_temperature: number;
}
    
export type DailyAvgRainAmoutType ={
    date: string;
    avg_rain_amount: number;
}

export type ClimateDataType = {
    first_datetime: string;
    last_datetime: string;
    max_temperature: number;
    min_temperature: number;
    avg_temperature: number;
    max_rain_amount: number;
    min_rain_amount: number;
    avg_rain_amount: number;
    max_pressure: number;
    min_pressure: number;
    avg_pressure:number;
    daily_avg_rain_amount: DailyAvgRainAmoutType[];
    daily_avg_temperatures: DailyAvgTemperatureType[];
}