import { BarChart, Bar, XAxis, YAxis } from 'recharts';
const data = [
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 400, pv: 600},
    {name: 'Page A', uv: 400, pv: 600},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},
    {name: 'Page A', uv: 300, pv: 200},

];

export function BarChartComponent() {
    return (
        <BarChart width={800} height={300} data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Bar dataKey="uv" barSize={10} fill="#8884d8"/>
          <Bar dataKey="pv" barSize={10} fill="#000"/>
        </BarChart>
    )
};

