// window.onload = function (arr_sost) {
//     document.getElementsByTagName('table')[0].addEventListener('click', function (e) {
//         let y = e.target.parentElement.rowIndex;
//         let x = e.target.cellIndex;
//         print_elem_sost(x, y, arr_sost);
//     }, false);
// }

function start() {
    // sost = [[]]
    let arr_sost = gen_table_and_arr_sost();
}

function check_in_arr_cell_complete(y, x, arr_sost, arr_cell_complete) {
    // Функция для того, чтобы установить, обрабатывалась ячейка или нет
    // Необходима с целью избежать бесконечного цикла или рекурсии, тк при перемещении индекса, не отмечала ячейку с которой пришел и возвращался к ней обратно
    for (let i = 0; i < arr_cell_complete.length; i++) {
        // console.log('arr_cell_complete[i] = ', arr_cell_complete[i], 'arr_sost[y][x] = ', Array(y, x));
        if (String(arr_cell_complete[i]) == String(Array(y, x))) {
            return (false);
        } else if ((arr_cell_complete != arr_sost[y][x]) && (i == arr_cell_complete.length - 1)) {
            return (true);
        }
    }
}

function check_cell_complete_in_table(table, arr_sost, y, x) {
    let arr_bomb = [];
    let schetchik_izvestnih = 0;
    try {
        let value_cell_this = table.rows[y - 1].cells[x].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y - 1][x] == 0) {
            arr_bomb.push(Array(y - 1, x));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y + 1][x] == 0) {
            arr_bomb.push(Array(y + 1, x));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y][x + 1] == 0) {
            arr_bomb.push(Array(y, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y][x - 1] == 0) {
            arr_bomb.push(Array(y, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y - 1].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y - 1][x - 1] == 0) {
            arr_bomb.push(Array(y - 1, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y - 1].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y - 1][x + 1] == 0) {
            arr_bomb.push(Array(y - 1, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y + 1][x - 1] == 0) {
            arr_bomb.push(Array(y + 1, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            schetchik_izvestnih++;
        }
        if (arr_sost[y + 1][x + 1] == 0) {
            arr_bomb.push(Array(y + 1, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    // console.log('ARR_SOST = ', arr_bomb);
    return [arr_bomb, schetchik_izvestnih];
}

function check_and_set_flag_table(table, arr_sost, y, x) {
    let cell_value = table.rows[y].cells[x].innerHTML;
    let arr_bomb = [];
    let schetchik_izvestnih = 0;
    let arr = check_cell_complete_in_table(table, arr_sost, y, x);
    arr_bomb = arr[0];
    schetchik_izvestnih = arr[1];
    if ((cell_value == "1") && (schetchik_izvestnih == 7)) {
        if (arr_bomb != undefined) {
            print_bomb(table, arr_bomb);
        }
    } else if ((cell_value == "2") && (schetchik_izvestnih == 6)) {
        if (arr_bomb != undefined) {
            print_bomb(table, arr_bomb);
        }
    } else if ((cell_value == "3") && (schetchik_izvestnih == 5)) {
        if (arr_bomb != undefined) {
            print_bomb(table, arr_bomb);
        }
    } else if ((cell_value == "4") && (schetchik_izvestnih == 4)) {
        if (arr_bomb != undefined) {
            print_bomb(table, arr_bomb);
        }
    }
}

// function bom_has_been_defused(table, arr_sost) {
//     let y = 0;
//     let x = 0;
//     for (let i = 0; i < 20; i++) {
//         y++;
//         for (let j = 0; j < 40; j++) {
//             x++;
//             try {
//                 let cell_value = table.rows[y].cells[x].innerHTML;
//                 let arr_bomb = [];
//                 let schetchik_izvestnih = 0;
//                 let arr = check_cell_complete_in_table(table, arr_sost, y, x);
//                 arr_bomb = arr[0];
//                 schetchik_izvestnih = arr[1];
//                 if ((cell_value == "1") && (schetchik_izvestnih == 7)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "2") && (schetchik_izvestnih == 6)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "3") && (schetchik_izvestnih == 5)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "4") && (schetchik_izvestnih == 4)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 }
//             } catch (error) {
//                 let cell_value = 'undef';
//                 let arr_bomb = [];
//                 let schetchik_izvestnih = 0;
//                 console.log('');
//                 let arr = check_cell_complete_in_table(table, arr_sost, y, x);
//                 arr_bomb = arr[0];
//                 schetchik_izvestnih = arr[1];
//                 if ((cell_value == "1") && (schetchik_izvestnih == 7)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "2") && (schetchik_izvestnih == 6)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "3") && (schetchik_izvestnih == 5)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 } else if ((cell_value == "4") && (schetchik_izvestnih == 4)) {
//                     if (arr_bomb != undefined) {
//                         print_bomb(table, arr_bomb);
//                     }
//                 }
//             }

//         }
//     }
// }

function print_bomb(table, arr_bomb) {
    // console.log('print_bomb');
    for (let i = 0; i < arr_bomb.length; i++) {
        // img = document.createElement('img');
        // img.src = 'Bombdefusal.png';
        // table.rows[arr_bomb[i][0]].cells[arr_bomb[i][1]].style = 'background-color: blue;'
        // table.rows[arr_bomb[i][0]].cells[arr_bomb[i][1]].appendChild(img);
        table.rows[arr_bomb[i][0]].cells[arr_bomb[i][1]].innerHTML = 'b';
        table.rows[arr_bomb[i][0]].cells[arr_bomb[i][1]].style = 'background-color: rgb(144, 232, 182);';
    }
}

function check_area_of_value(table, y, x, arr_sost, arr_cell_complete) {
    let arr_bomb = [];
    let schetchik_izvestnih = 0;
    try {
        let value_cell_this = table.rows[y - 1].cells[x].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y - 1, x, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y - 1][x] == 0) {
            arr_bomb.push(Array(y - 1, x));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y + 1, x, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y + 1][x] == 0) {
            arr_bomb.push(Array(y + 1, x));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y, x + 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y][x + 1] == 0) {
            arr_bomb.push(Array(y, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y, x - 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y][x - 1] == 0) {
            arr_bomb.push(Array(y, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y - 1].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y - 1, x - 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y - 1][x - 1] == 0) {
            arr_bomb.push(Array(y - 1, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y - 1].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y - 1, x + 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y - 1][x + 1] == 0) {
            arr_bomb.push(Array(y - 1, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x - 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y + 1, x - 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y + 1][x - 1] == 0) {
            arr_bomb.push(Array(y + 1, x - 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    try {
        let value_cell_this = table.rows[y + 1].cells[x + 1].innerHTML;
        if ((value_cell_this == 'c') || (value_cell_this == '1') || (value_cell_this == '2') || (value_cell_this == '3') || (value_cell_this == '4')) {
            if ((value_cell_this == 'c') && !(check_in_arr_cell_complete(y + 1, x + 1, arr_sost, arr_cell_complete))) {
                schetchik_izvestnih++;
            } else if (value_cell_this != '') {
                schetchik_izvestnih++;
            }
        }
        if (arr_sost[y + 1][x + 1] == 0) {
            arr_bomb.push(Array(y + 1, x + 1));
        }
    } catch (error) {
        schetchik_izvestnih++;
    }
    // console.log('ARR_SOST = ', arr_bomb);
    return [arr_bomb, schetchik_izvestnih];
}

function check_and_set_flag(table, arr_sost, arr_numbers_maybe_to_flag, arr_cell_complete) {
    for (let i = 0; i < arr_numbers_maybe_to_flag.length; i++) {
        let y = arr_numbers_maybe_to_flag[i][0];
        let x = arr_numbers_maybe_to_flag[i][1];
        let cell_value = table.rows[y].cells[x].innerHTML;
        let arr_bomb = [];
        let schetchik_izvestnih = 0;
        let arr = check_area_of_value(table, y, x, arr_sost, arr_cell_complete);
        arr_bomb = arr[0];
        schetchik_izvestnih = arr[1];
        if ((cell_value == "1") && (schetchik_izvestnih == 7)) {
            if (arr_bomb != undefined) {
                print_bomb(table, arr_bomb);
            }
        } else if ((cell_value == "2") && (schetchik_izvestnih == 6)) {
            if (arr_bomb != undefined) {
                print_bomb(table, arr_bomb);
            }
        } else if ((cell_value == "3") && (schetchik_izvestnih == 5)) {
            if (arr_bomb != undefined) {
                print_bomb(table, arr_bomb);
            }
        } else if ((cell_value == "4") && (schetchik_izvestnih == 4)) {
            if (arr_bomb != undefined) {
                print_bomb(table, arr_bomb);
            }
        }

        // if (String(arr_numbers_maybe_to_flag[i]) == String(sost[y, x])) {

        // }
    }
}

function set_empty_cell(table, y, x, new_arr_empty, arr_cell_complete) {
    // Функция для заполнения пустых ячеек
    table.rows[y].cells[x].innerHTML = 'c';
    table.rows[y].cells[x].style = 'font-size: 0.01px; background-color: rgb(189, 192, 194);';
    new_arr_empty.push(Array(y, x));
    arr_cell_complete.push(Array(y, x));
    return (new_arr_empty, arr_cell_complete);
}

function check_empty_cells(y, x, arr_sost, arr_empty, arr_cell_complete, arr_numbers_maybe_to_flag) {
    let table = document.getElementById('table');
    let new_arr_empty = [];
    if (arr_empty == undefined) {
        arr_empty = [];
    }
    if (arr_numbers_maybe_to_flag == undefined) {
        arr_numbers_maybe_to_flag = [];
    }

    if (arr_empty.length == 0) {
        arr_empty.push('clear');
    }

    for (let i = 0; i < arr_empty.length; i++) {

        if (arr_empty[0] != 'clear') {
            y = Number(arr_empty[i][0]);
            x = Number(arr_empty[i][1]);
        } else if (arr_empty[0] == 'clear') {

        }

        try {
            if (check_in_arr_cell_complete(y - 1, x, arr_sost, arr_cell_complete)) {
                if (arr_sost[y - 1][x] == 9) {
                    new_arr_empty,
                    arr_cell_complete = set_empty_cell(table, y - 1, x, new_arr_empty, arr_cell_complete);
                }
                else if ((arr_sost[y - 1][x] != 9) && ((arr_sost[y - 1][x] != 0))) {
                    table.rows[y - 1].cells[x].innerHTML = arr_sost[y - 1][x];
                    arr_numbers_maybe_to_flag.push(Array(y - 1, x));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y + 1, x, arr_sost, arr_cell_complete)) {
                if (arr_sost[y + 1][x] == 9) {
                    new_arr_empty,
                    arr_cell_complete = set_empty_cell(table, y + 1, x, new_arr_empty, arr_cell_complete);
                }
                else if ((arr_sost[y + 1][x] != 9) && ((arr_sost[y + 1][x] != 0))) {
                    table.rows[y + 1].cells[x].innerHTML = arr_sost[y + 1][x];
                    arr_numbers_maybe_to_flag.push(Array(y + 1, x));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y, x - 1, arr_sost, arr_cell_complete)) {
                if (arr_sost[y][x - 1] == 9) {
                    new_arr_empty,
                    arr_cell_complete = set_empty_cell(table, y, x - 1, new_arr_empty, arr_cell_complete);
                }
                else if ((arr_sost[y][x - 1] != 9) && ((arr_sost[y][x - 1] != 0))) {
                    table.rows[y].cells[x - 1].innerHTML = arr_sost[y][x - 1];
                    arr_numbers_maybe_to_flag.push(Array(y, x - 1));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y, x + 1, arr_sost, arr_cell_complete)) {
                if (arr_sost[y][x + 1] == 9) {
                    new_arr_empty,
                    arr_cell_complete = set_empty_cell(table, y, x + 1, new_arr_empty, arr_cell_complete);
                }
                else if ((arr_sost[y][x + 1] != 9) && ((arr_sost[y][x + 1] != 0))) {
                    table.rows[y].cells[x + 1].innerHTML = arr_sost[y][x + 1];
                    arr_numbers_maybe_to_flag.push(Array(y, x + 1));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y - 1, x + 1, arr_sost, arr_cell_complete)) {
                if ((arr_sost[y - 1][x + 1] != 9) && ((arr_sost[y - 1][x + 1] != 0))) {
                    table.rows[y - 1].cells[x + 1].innerHTML = arr_sost[y - 1][x + 1];
                    arr_numbers_maybe_to_flag.push(Array(y - 1, x + 1));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y + 1, x - 1, arr_sost, arr_cell_complete)) {
                if ((arr_sost[y + 1][x - 1] != 9) && ((arr_sost[y + 1][x - 1] != 0))) {
                    table.rows[y + 1].cells[x - 1].innerHTML = arr_sost[y + 1][x - 1];
                    arr_numbers_maybe_to_flag.push(Array(y + 1, x - 1));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y - 1, x - 1, arr_sost, arr_cell_complete)) {
                if ((arr_sost[y - 1][x - 1] != 9) && ((arr_sost[y - 1][x - 1] != 0))) {
                    table.rows[y - 1].cells[x - 1].innerHTML = arr_sost[y - 1][x - 1];
                    arr_numbers_maybe_to_flag.push(Array(y - 1, x - 1));
                }
            }
        } catch (error) {}
        try {
            if (check_in_arr_cell_complete(y + 1, x + 1, arr_sost, arr_cell_complete)) {
                if ((arr_sost[y + 1][x + 1] != 9) && ((arr_sost[y + 1][x + 1] != 0))) {
                    table.rows[y + 1].cells[x + 1].innerHTML = arr_sost[y + 1][x + 1];
                    arr_numbers_maybe_to_flag.push(Array(y + 1, x + 1));
                }
            }
        } catch (error) {}
    }

    if (new_arr_empty.length != 0) {
        check_empty_cells(y, x, arr_sost, new_arr_empty, arr_cell_complete, arr_numbers_maybe_to_flag);
    } else if (new_arr_empty.length == 0) {
        check_and_set_flag(table, arr_sost, arr_numbers_maybe_to_flag, arr_cell_complete);
    }
}

function check_and_set_value(x, y, arr_sost) {
    let count = 0;
    try {
        if (arr_sost[y - 1][x] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y + 1][x] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y][x - 1] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y][x + 1] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y - 1][x + 1] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y + 1][x - 1] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y - 1][x - 1] == 0) {
            count++;
        }
    } catch (error) {}
    try {
        if (arr_sost[y + 1][x + 1] == 0) {
            count++;
        }
    } catch (error) {}
    return (count);
}

function end_game() {
    let table = document.getElementById('table');
    table.parentNode.removeChild(table);
    h2 = document.createElement('h2');
    h2.innerHTML = 'Game over)';
    document.getElementById('saper').after(h2);
}

function print_all_field(arr_sost) {
    let table = document.getElementById('table');
    for (let x = 0; x < 20; x++) {
        for (let y = 0; y < 40; y++) {
            if (arr_sost[x][y] == 0) {
                table.rows[x].cells[y].innerHTML = '';
                img = document.createElement('img');
                img.src = 'C:/Users/Денис/Desktop/Курсы по Django/mysite/games/static/games/img/Bombdefusal.png';
                table.rows[x].cells[y].style = 'background-color: red;'
                table.rows[x].cells[y].appendChild(img);
            } else if (arr_sost[x][y] == 9) {
                table.rows[x].cells[y].innerHTML = '';
            } else {
                table.rows[x].cells[y].innerHTML = arr_sost[x][y];
            }
        }
    }
    setTimeout(() => {
        end_game();
        // console.log(arr_sost);
    }, 10000);
}

function reset() {
    document.getElementById('body').innerHTML = '';
    gen_table_and_arr_sost();
}

function gen_table_and_arr_sost() {
    let arr_sost = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ];
    // Создает таблицу 20 на 40 и генерит массив 20 на 40
    let table = document.createElement('table');
    table.setAttribute("id", "table");
    for (let i = 0; i < 20; i++) {
        tr = document.createElement('tr');
        for (let j = 0; j < 40; j++) {
            td = document.createElement('td');
            td.setAttribute("class", "cell");
            td.setAttribute("onclick", "click1(this)");
            td.setAttribute("id", 'id' + i + j);
            td.innerHTML = '';
            tr.appendChild(td);
            arr_sost[i].push(Math.floor(Math.random() * 7));
        }
        table.appendChild(tr);
    }

    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 40; j++) {
            if (arr_sost[i][j] != 0) {
                let count = check_and_set_value(j, i, arr_sost);
                if (count == 0) {
                    arr_sost[i][j] = 9;
                } else {
                    arr_sost[i][j] = count;
                }
            }
        }
    }

    let btn_reset = document.createElement('button');
    let h2 = document.createElement('h2');
    h2.innerHTML = 'Saper';
    h2.setAttribute("id", "saper");
    btn_reset.setAttribute("onclick", "reset()");
    btn_reset.setAttribute("id", "btn");
    btn_reset.innerHTML = "Новая игра";
    document.getElementById('body').appendChild(h2);
    document.getElementById('body').appendChild(table);
    document.getElementById('body').appendChild(btn_reset);
    localStorage.setItem('arr_sost', arr_sost);
    // console.log(arr_sost);

    return (arr_sost);
}

function click_repeat(table, arr_sost) {
    let y = 0;
    let x = 0;
    let arr_with_indexes = [];
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 40; j++) {
            try {
                let cell_value = table.rows[y].cells[x].innerHTML;
                if ((cell_value == "1") || (cell_value == "2") || (cell_value == "3") || (cell_value == "4")) {
                    arr_with_indexes.push(Array(Array(y, x), Array(cell_value)));
                    
                }
                x++;
            } catch {}
        }
        x = 0;
        y++;
    }
    console.log('arr_with_indexes = ', arr_with_indexes)
    if (arr_with_indexes.length != 0) {
        for (let i = 0; i < arr_with_indexes.length; i++) {
            
            let indexes = arr_with_indexes[i][0];
            console.log('indexes = ', indexes);
            y = Number(indexes[0]);
            x = Number(indexes[1]);
            cell_value = String(arr_with_indexes[i][1]);
            console.log('in_work y = ', y, 'x = ', x);

            let arr = check_cell_complete_in_table(table, arr_sost, y, x);
            let arr_bomb = arr[0];
            let schetchik_izvestnih = Number(arr[1]);
            if ((cell_value == "1") && (schetchik_izvestnih == 7)) {
                if (arr_bomb != undefined) {
                    print_bomb(table, arr_bomb);
                }
            } else if ((cell_value == "2") && (schetchik_izvestnih == 6)) {
                if (arr_bomb != undefined) {
                    print_bomb(table, arr_bomb);
                }
            } else if ((cell_value == "3") && (schetchik_izvestnih == 5)) {
                if (arr_bomb != undefined) {
                    print_bomb(table, arr_bomb);
                }
            } else if ((cell_value == "4") && (schetchik_izvestnih == 4)) {
                if (arr_bomb != undefined) {
                    print_bomb(table, arr_bomb);
                }
            }
        }
    }
}

function print_elem_sost(x, y, arr_sost) {
    let table = document.getElementById('table');
    let a = localStorage.getItem('arr_sost');
    arr_sost = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ];
    a = a.split(',');
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 40; j++) {
            arr_sost[i][j] = Number(a[0]);
            a.shift();
        }
    }

    let arr_cell_complete = [];

    if (arr_sost[y][x] == 0) {
        print_all_field(arr_sost);
    } else if (arr_sost[y][x] == 9) {
        table.rows[y].cells[x].innerHTML = 'c';
        arr_cell_complete.push(Array(y, x));
        table.rows[y].cells[x].style = 'font-size:0.01px; background-color: rgb(189, 192, 194);'
        check_empty_cells(y, x, arr_sost, undefined, arr_cell_complete);
        console.log('before y = ', y, 'x = ', x);
        click_repeat(table, arr_sost);
        // bom_has_been_defused(table, arr_sost);
    } else {
        console.log('before y = ', y, 'x = ', x);
        table.rows[y].cells[x].innerHTML = arr_sost[y][x];
        check_and_set_flag_table(table, arr_sost, y, x);
        click_repeat(table, arr_sost);
        // bom_has_been_defused(table, arr_sost);

    }

    // let arr_cell_complete_history = [1, 2, 3];
    // localStorage.setItem('arr_cell_complete_history', arr_cell_complete_history);
    // console.log('local = ', localStorage.getItem('arr_cell_complete_history'));
    //     if ((arr_cell_complete.length != 0) && (localStorage.getItem('arr_cell_complete_history') !== null)) {
    //         let a = localStorage.getItem('arr_cell_complete_history');

    //         console.log('a = ', a);
    //         a.split(',');
    //         console.log('a = ', a);
    //         for (let i = 0; i < arr_cell_complete.length; i++) {
    //             arr_cell_complete_history.push(1);
    //             if (i == 0) {
    //                 arr_cell_complete_history[i] = Array(a[i], a[i + 1]);
    //             } else {
    //                 arr_cell_complete_history[i] = Array(a[i + 1], a[i + 2]);
    //                 // console.log('arr_cell_complete_history in cicle 1= ', arr_cell_complete_history);
    //             }
    //         }
    //         localStorage.setItem('arr_cell_complete_history', arr_cell_complete_history);
    //     } else {
    //         localStorage.setItem('arr_cell_complete_history', arr_cell_complete);
    //     }

    //     console.log('arr_cell_complete_history = ', arr_cell_complete_history);


}

function click1(cell) {
    let x = cell.cellIndex;
    let y = cell.parentElement.rowIndex;
    print_elem_sost(x, y);
}

start();
