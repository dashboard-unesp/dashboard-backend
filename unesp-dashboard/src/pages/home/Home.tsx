import { DatePickerWithRange } from '@/components/date-range-selection/DateRangeSelector';
import './Home.css';
import { SearchOptions } from '@/components/dashboard-search-options/DashboardSearchOptions';
import { Input } from '@/components/ui/input';
import { DashboardTable } from '@/components/dashboard-table/DashboardTable';

function Home(){
    return (
        <div className='dashboard-container'>
            <nav className='dashboard-header'>
                <SearchOptions />
                <Input />
                <DatePickerWithRange />
            </nav>
            <main className='table-container'>
                <DashboardTable />
            </main>
            <section className='chart-container'>
                <div className='bar-chart-container'>
                    <SearchOptions />
                </div>
                <div className='donut-chart-container'>
                    <SearchOptions />
                </div>
            </section>
        </div>
    );
}

export default Home;