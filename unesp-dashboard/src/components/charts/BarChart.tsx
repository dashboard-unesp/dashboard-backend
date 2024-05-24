import { format, formatDate, subDays } from 'date-fns';
import { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';

const data1 = [
    {name: 'Page A', minTemp: 300.50, maxTemp: 200},
    {name: 'Page A', minTemp: 400, maxTemp: 600},
    {name: 'Page A', minTemp: 400, maxTemp: 600},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
    {name: 'Page A', minTemp: 300, maxTemp: 200},
];

const legendStyle: React.CSSProperties = { 
    bottom: 0, 
    backgroundColor: '#f5f5f5',
    border: '1px solid #d5d5d5', 
    borderRadius: 3, 
    lineHeight: '40px',
    gap: '10px',
    justifyContent: 'center',
}

// async function fetchData() {
//     let today = format(new Date(), 'y-MM-dd');
//     let responses = [];
//     for(let i = 0; i < 10; i++){
//         let filterEnd = format(subDays(today, i), 'y-MM-dd');
//         let filterStart = format(subDays(filterEnd, i), 'y-MM-dd');
//         fetch(`http://localhost:8000/filter/${filterStart}/${filterEnd}`, {mode: 'no-cors'})
//         .then(response => response.json())
//         .then(data => responses.push(data));
//     }
//     return responses;
// }

export function BarChartComponent() {

    const [data, setData] = useState<any[]>([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
  
    const fetchData = async (filterStart: string, filterEnd: string) => {
        setIsLoading(true);
        setError(null); // Clear any previous errors
        try {
            const fetchedData = await fetch(`http://localhost:8000/filter/2024-01-15/${filterEnd}?format=json`, {
                method: 'GET',  // Example for a POST request
                headers: {
                    'Access-Control-Allow-Origin' : 'http://localhost:5173'
                }
            });
            //const fetchedData = await response.json();
            console.log(fetchedData)
            //setData([data, ...fetchedData]);
        } catch (error: any) {
            console.log(error)
            setError(error.message);
        } finally {
            setIsLoading(false);
        }
    };
  
    useEffect(() => {
        let today = format(new Date(), 'y-MM-dd');
        for(let i = 0; i < 10; i++){
            let filterEnd = format(subDays(today, i), 'y-MM-dd');
            let filterStart = format(subDays(today, i +1 ), 'y-MM-dd');
            fetchData(filterStart, filterEnd);
        }
    }, []);

    return (
        <BarChart width={800} height={300} data={data}>
          <XAxis dataKey="name" />
          <YAxis  />
          <Tooltip />
          <Legend wrapperStyle={legendStyle} payload={[
                { value: 'Temperatura minima', type: 'square', id: 'ID01', color:'#8884d8' },
                { value: 'Temperatura maxima', type: 'square', id: 'ID02', color:'#000' }
            ]}/>
          <Bar dataKey="minTemp" barSize={10} fill="#8884d8"/>
          <Bar dataKey="maxTemp" barSize={10} fill="#000"/>
        </BarChart>
    )
};

