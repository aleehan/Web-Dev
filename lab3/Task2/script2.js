const listContainer = document.getElementById("tasks-list");
const inputBox = document.getElementById("task-input");
const addButton = document.getElementById("adding-button");

const addTask = () => {
    let newTaskValue = inputBox.value;
    
    if (newTaskValue === "") {
        alert("Please enter a task");
        return;
    }
    
    // const allTasks = listContainer.querySelectorAll('li');
    
    else {
        let li = document.createElement("li")
        li.className = "tasks-list-item";

        let divContent = document.createElement("div");
        divContent.className = "tasks-list-item-content";

        let label = document.createElement("label");
        label.className = "tasks-list-item-content-label";

        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.className = "tasks-list-item-content-checkbox";

        label.appendChild(checkbox);

        let taskName = document.createElement("p");
        taskName.className ="tasks-list-item-content-name";
        taskName.textContent = inputBox.value;

        divContent.appendChild(label);
        divContent.appendChild(taskName);

        let divFunctions = document.createElement("div");
        divFunctions.className = "tasks-list-item-functions";

        let deleteButton = document.createElement("button");
        deleteButton.className = "tasks-list-item-functions-button";
        deleteButton.type = "button";
        deleteButton.innerHTML = `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19 6V20C19 20.5304 18.7893 21.0391 18.4142 21.4142C18.0391 21.7893 17.5304 22 17 22H7C6.46957 22 5.96086 21.7893 5.58579 21.4142C5.21071 21.0391 5 20.5304 5 20V6" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
              <path d="M3 6H21" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
              <path d="M8 6V4C8 3.46957 8.21071 2.96086 8.58579 2.58579C8.96086 2.21071 9.46957 2 10 2H14C14.5304 2 15.0391 2.21071 15.4142 2.58579C15.7893 2.96086 16 3.46957 16 4V6" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>`

        divFunctions.appendChild(deleteButton);

        li.appendChild(divContent);
        li.appendChild(divFunctions);

        listContainer.appendChild(li);
    }
    inputBox.value = "";
    saveData();
}

addButton.addEventListener("click", (e) => {
    addTask();
});

inputBox.addEventListener("keydown", (e) => {
    if(e.key === "Enter") {
        addTask();
        saveData();
    }
})

listContainer.addEventListener("click", (e) => {
    if(e.target.classList.contains("tasks-list-item-content-checkbox")) {
        e.target.closest("li").classList.toggle("completed");
        saveData();
    }
    if(e.target.closest(".tasks-list-item-functions-button")) {
        e.target.closest("li").remove();
        saveData();
    }
}); 

const saveData = () => {
    localStorage.setItem("task", listContainer.innerHTML);
}

const showList = () => {
    listContainer.innerHTML = localStorage.getItem("task") || "";
}

showList();


