function add_active() {
    // 
    // Функция для выделения подпункта меню для текущей страницы.
    // 
    let url_path = document.location.href;
    url_path = url_path.split('/');
    let list_items = ['ourteam', 'photo', 'reviews', 'video', 'aragats', 'ararat', 'elbrus', 'kazbek', 'kilimanjaro', 'lenin_peak', 'manaslu', 'monblan', 'peak_separate', 'arcticles', 'clothes_and_equuipment', 'phisical_training', 'question_answer', 'treaties', 'arround_annapurna', 'lician_path']
    let current_item = url_path[url_path.length - 1];

    function check_in_list(current_item, list_items) {
        for (let i = 0; i < list_items.length; i++) {
            if (current_item == list_items[i]) {
                return (true);
            }
        }
    }

    function setItemAttribute(current_item, list_items) {
        if (check_in_list(current_item, list_items)) {
            item = document.getElementById(current_item);
            item.classList.add('active');
        }
    }
    setItemAttribute(current_item, list_items);
}

add_active();


function align_right() {

    const mediaQuery = window.matchMedia('(max-width: 767px)')

    if (mediaQuery.matches) {
        // alert('Media Query Matched!')
        let bw = document.getElementById('bw');
        bw.classList.remove('justify-content-center');
        bw.classList.add('justify-content-start');
    }
    // let bw = document.getElementById('bw');
    // bw
    // .d-flex.justify-content-center.my-brand{

}

align_right();

function hidden_body(burger) {
    a = burger.classList[1];
    let body = document.getElementById('body');
    // let body = document.getElementsByTagName('body');

    if (a != 'collapsed') {
        body.style.overflow = 'hidden';
    } else {
        body.style.overflow = 'visible';
    }
}

// hidden_body();