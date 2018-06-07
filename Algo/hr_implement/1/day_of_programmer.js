function get_day_of_programmer(year) {
    let day_of_programmer = '13.09.';
    if (year == 1918) {
        day_of_programmer = '26.09.';
    } else if ((year < 1918 && year % 4 == 0) || ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))) {
        day_of_programmer = '12.09.';
    }
    return day_of_programmer + year;
}

console.log(get_day_of_programmer(1800));