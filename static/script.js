document.addEventListener("DOMContentLoaded",()=>{

    console.log("COVID AI Predictor Loaded");

    const form=document.querySelector("form");

    if(form){

        form.addEventListener("submit",()=>{

            document.querySelector("button").innerText =
            "Predicting...";

        });

    }

});