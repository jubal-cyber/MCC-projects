const questions = [

{
    question: "The data structure required for Breadth First Traversal on a graph is??",
    options: [
        "Array", 
        "stack", "tree", "queue"
    ],
    answer: "queue"
},

  


{
    question: "What data structure would you mostly likely see in non recursive implementation of a recursive algorithm?",
    options: ["stack", "linked list", "tree", "queue"],
    answer: "stack"
},

{
    question: "Which data structure is needed to convert infix notation to postfix notation?",
    options: ["stack", "linked list", "tree", "queue"],
    answer: "stack"
}

];

questions.sort(() => Math.random() - 0.5);

let currentQuestion = 0;
let score = 0;
let selectedAnswer = "";

const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const nextBtn = document.getElementById("nextBtn");
const restartBtn = document.getElementById("restartBtn");
const scoreEl = document.getElementById("score");

function loadQuestion(){

    selectedAnswer = "";

    const current = questions[currentQuestion];

    questionEl.textContent = current.question;

    optionsEl.innerHTML = "";

    current.options.forEach(option => {

        const div = document.createElement("div");

        div.classList.add("option");

        div.textContent = option;

        div.onclick = () => {

            selectedAnswer = option;

            document.querySelectorAll(".option").forEach(opt => {
                //remove highlight from pre choice//
                opt.classList.remove("selected");
            });
            //highlight select color//
            div.classList.add("selected");
        };
        //adding options//
        optionsEl.appendChild(div);
    });
}

nextBtn.onclick = () => {
    //ans check//
    if(selectedAnswer === questions[currentQuestion].answer){
        score++;
    }
    //score refresh//
    scoreEl.textContent = `Score: ${score}`;

    currentQuestion++;
    //if still q load q// 
    if(currentQuestion < questions.length){

        loadQuestion();

    } else {
//result pop//
        alert(`Quiz Finished!\nYour Score: ${score}/${questions.length}`);

        questionEl.textContent = "Quiz Completed!";

        optionsEl.innerHTML = "";

        nextBtn.style.display = "none";

        restartBtn.style.display = "block";
    }
};

restartBtn.onclick = () => {

    currentQuestion = 0;

    score = 0;

    selectedAnswer = "";
//re shuffle q//
    questions.sort(() => Math.random() - 0.5);

    scoreEl.textContent = "Score: 0";

    nextBtn.style.display = "block";

    restartBtn.style.display = "none";

    loadQuestion();
};

loadQuestion();