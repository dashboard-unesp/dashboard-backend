import { format } from 'date-fns';
import { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';

type BarChartData = {
    datetime: string;
    minTemp: number;
    maxTemp: number;
}

const { VITE_API_URL } = import.meta.env

// const data1 = [
//     {name: 'Page A', minTemp: 300.50, maxTemp: 200},
//     {name: 'Page A', minTemp: 400, maxTemp: 600},
//     {name: 'Page A', minTemp: 400, maxTemp: 600},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
//     {name: 'Page A', minTemp: 300, maxTemp: 200},
// ];

const legendStyle: React.CSSProperties = { 
    bottom: 0, 
    backgroundColor: '#f5f5f5',
    border: '1px solid #d5d5d5', 
    borderRadius: 3, 
    lineHeight: '40px',
    gap: '10px',
}

export function BarChartComponent() {

    const [data, setData] = useState<any[]>([]);
  
    const fetchData = async (filterStart: string, filterEnd: string) => {
        
        try {
            const params = (filterStart && filterEnd) 
            ? `?date_from=${filterStart}&date_to=${filterEnd}&format=json`
            : `?date_from=2024-03-01&date_to=2024-03-28&format=json`;
            
            console.log(params)
            
            const response = await fetch(`${VITE_API_URL}/climate/barchart/${params}`, {
                method: 'GET',  
            }).then(response => response.json());

            const data = response.map(({datetime, minTemp, maxTemp}:BarChartData) => {
                return {
                    name: format(datetime, 'd-M'),
                    minTemp: minTemp.toFixed(0),
                    maxTemp: maxTemp.toFixed(0)
                }
            })
            setData(data)
            
        } catch (error: any) {
            console.log(error)
        } 
    };
  
    useEffect(() => {
        
        fetchData('','');
    }, []);

    return (
        <BarChart width={800} height={300} data={data}>
          <XAxis dataKey="name" />
          <YAxis  />
          <Tooltip />
          <Legend wrapperStyle={legendStyle} payload={[
                { value: 'Temperatura minima', type: 'square', id: 'ID01', color:'#8884d8' },
                { value: 'Temperatura maxima', type: 'square', id: 'ID02', color:'#000' }
            ]} />
          <Bar dataKey="minTemp" barSize={10} fill="#8884d8"/>
          <Bar dataKey="maxTemp" barSize={10} fill="#000"/>
        </BarChart>
    )
};

