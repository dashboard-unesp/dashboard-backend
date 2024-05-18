import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';
const data = [
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

export function BarChartComponent() {
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
