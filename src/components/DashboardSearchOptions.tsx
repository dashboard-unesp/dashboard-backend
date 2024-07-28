import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover";

export function SearchOptions(){
    return(
        <Popover>
            <PopoverTrigger>Search</PopoverTrigger>
            <PopoverContent> 
                Place content for the popover here.
            </PopoverContent>
        </Popover>
    );
}
  