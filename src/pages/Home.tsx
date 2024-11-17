import { DatePickerWithRange } from '@/components/DateRangeSelector';
import { SearchOptions } from '@/components/DashboardSearchOptions';
import { Input } from '@/components/ui/input';
import { DashboardTable } from '@/components/DashboardTable';
import { TemperatureChartComponent } from '@/components/charts/TemperatureChart';
import { RainChartComponent } from '@/components/charts/RainChart';
import { useEffect, useState } from 'react';
import { ClimateDataType } from '@/types/Climate';
import useToken from '@/hooks/useToken';


const { VITE_API_URL } = import.meta.env

function Home(){
    const {token, setToken} = useToken();
    const [dailyClimateData, setDailyClimateData] = useState<ClimateDataType>();
  
    const fetchData = async () => {
        
        try {
                   
            const data = await fetch(`${VITE_API_URL}/climate/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Token ${token}`
                }  
            }).then(response => response.json());

            setDailyClimateData(data)
    
        } catch (error: any) {
            console.error(error)
        } 
    };
  
    useEffect(() => {
        fetchData();
    }, []);

    return (
        <section className='px-8 py-[2%] bg-white w-full'>
            <nav className='flex justify-end gap-[10px] w-full pb-4'>
                <SearchOptions />
                <Input />
                <DatePickerWithRange />
            </nav>
            <main className='px-[2%] pb-[5%]'>
                <DashboardTable />
            </main>
            <section className='flex flex-row items-center p-4 justify-between'>
                {   
                    dailyClimateData 
                        ?
                            <>
                                <div className='max-w-[60%]'>
                                    <TemperatureChartComponent data={dailyClimateData.daily_avg_temperatures}/>
                                </div>
                                <div className='max-w-[40%]'>
                                    <RainChartComponent data={dailyClimateData.daily_avg_rain_amount}/>
                                </div> 
                            </> 
                        : <></>
                }
            </section>
        </section>
    );
}

export default Home;