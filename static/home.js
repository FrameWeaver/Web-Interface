const script_input = document.getElementsByClassName("script")[0];
const uploadButton = document.getElementById("script_upload");
const loading = document.getElementById("progress_bar_container")


const form = document.getElementById("form")
console.log(form)

uploadButton.addEventListener("click", (event)=>{
    event.preventDefault();
    console.log("clicked")
    script_input.click();
})

script_input.addEventListener("change", ()=>{

    const data = new FormData(form);
    loading.style.display = "flex"
    uploadButton.style.display = "none"
    fetch("/upload_script" , {

        method : "POST", 
        body : data
    }

  

    ).then((response)=>{
        
        return response.json()
    }).then((responseJson)=>{

        console.log(responseJson)
        filename =  responseJson['filename']
        window.location.href = `/output/${filename}`
    })

})