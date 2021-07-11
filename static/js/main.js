import tablecsv from "./tablecsv.js";

const tableRoot = document.querySelector("#root");
const csvfileinput =document.querySelector("#csvfileinput");
const Tablecsv = new tablecsv(tableRoot);

csvfileinput.addEventListener("change", e=>{
    
    Papa.parse(csvfileinput.files[0], {
        delimiter: ",",
        skipEmptyLines:true,
        complete: results => {
            Tablecsv.update(results.data.slice(1), results.data[0])
            
        }
    })

});



