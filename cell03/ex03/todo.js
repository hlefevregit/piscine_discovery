// Fonction pour obtenir un cookie par nom
function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    for(let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        if(name === cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

// Fonction pour définir un cookie
function setCookie(name, value, days) {
    let date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    let expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + encodeURIComponent(value) + ";" + expires + ";path=/";
}

// Fonction pour sauvegarder les tâches dans un cookie
function saveTasks() {
    let tasks = [];
    document.querySelectorAll('.todo-item').forEach(function(task) {
        tasks.push(task.textContent);
    });
    setCookie('tasks', JSON.stringify(tasks), 7);
}

// Fonction pour charger les tâches à partir d'un cookie
function loadTasks() {
    let tasks = getCookie('tasks');
    if (tasks) {
        JSON.parse(tasks).forEach(function(task) {
            addTaskToDOM(task);
        });
    }
}

// Fonction pour ajouter une tâche au DOM
function addTaskToDOM(task) {
    let taskDiv = document.createElement('div');
    taskDiv.textContent = task;
    taskDiv.className = 'todo-item';
    taskDiv.addEventListener('click', function() {
        if (confirm('Voulez-vous supprimer cette tache ?')) {
            taskDiv.remove();
            saveTasks();
        }
    });
    let ftList = document.getElementById('ft_list');
    ftList.insertBefore(taskDiv, ftList.firstChild);
}

document.getElementById('new-button').addEventListener('click', function() {
    let task = prompt('Nouvelle tache :');
    if (task && task.trim() !== '') {
        addTaskToDOM(task);
        saveTasks();
    }
});

// Charger les tâches au démarrage
window.onload = loadTasks;