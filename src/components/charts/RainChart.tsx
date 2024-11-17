import { Button } from '@/components/ui/button';
import { DailyAvgRainAmoutType } from '@/types/Climate';
import { PieChart, Pie, Legend, Tooltip } from 'recharts';

interface ColorMap {
  [key: number]: string;
}

const colorMap: ColorMap = {
  0: '#FF6384',
  1: '#36A2EB',
  2: '#FFCE56',
  3: '#4BC0C0',
  4: '#9966FF',
  5: '#FF9F40',
  6: '#F08080',
  7: '#9ACD32',
  8: '#BA55D3',
  9: '#CD853F'
};

export function RainChartComponent({data}:{data:DailyAvgRainAmoutType[]}){
    // TODO:

    const cleanData = data.map((value) => {
        return {
          'name': value.date,
          'value': value.avg_rain_amount,
          'fill': colorMap[data.indexOf(value)]
        }
    }).slice(-5);

    return (
      <div className='flex flex-col items-center'>
        <header className='flex flex-row justify-around w-full'>
          <div>
            <h2>Probabilidade de precipitação</h2>
            <p className='font-thin'>De {cleanData[0].name} - {cleanData[cleanData.length - 1].name}</p>
          </div>
          <Button className='text-[var(--theme-font-color)] bg-white hover:bg-white font-bold'>Ver relatório</Button>
        </header>
        <div className='h-fit'>
            <PieChart width={250} height={250}>
              <Pie data={cleanData}
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

