import { Button } from '@/components/ui/button';
import { PieChart, Pie, Legend, Tooltip } from 'recharts';

const data = [
  { name: 'Group A', value: 800, fill: '#8884d8' },
  { name: 'Group B', value: 300, fill: '#000'},
  { name: 'Group C', value: 300, fill: '#D3D1F2' },
  { name: 'Group D', value: 200, fill: '#7E7CEC ' },
];

export function DonutChartComponent(){
  
    return (
      <div className='flex flex-col items-center'>
        <header className='flex flex-row justify-around w-full'>
          <div>
            <h2>Probabilidade de precipitação</h2>
            <p className='font-thin'>De 01 de maio - 05 de maio de 2024</p>
          </div>
          <Button className='text-[var(--theme-font-color)] bg-white hover:bg-white font-bold'>Ver relatório</Button>
        </header>
        <div className='h-fit'>
            <PieChart width={250} height={250}>
              <Pie data={data}
                cx="50%" cy="50%"
                innerRadius={60}
                outerRadius={80}
                dataKey="value"
              />
              <Tooltip />
              <Legend />
            </PieChart>
        </div>
      </div>
    );
};

