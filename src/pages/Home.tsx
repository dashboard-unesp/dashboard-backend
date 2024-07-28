import { DatePickerWithRange } from '@/components/DateRangeSelector';
import { SearchOptions } from '@/components/DashboardSearchOptions';
import { Input } from '@/components/ui/input';
import { DashboardTable } from '@/components/DashboardTable';
import { BarChartComponent } from '@/components/charts/BarChart';
import { DonutChartComponent } from '@/components/charts/DonutChart';

function Home(){
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
                <div className='max-w-[60%]'>
                    <BarChartComponent />
                </div>
                <div className='max-w-[40%]'>
                    <DonutChartComponent />
                </div>
            </section>
        </section>
    );
}

export default Home;