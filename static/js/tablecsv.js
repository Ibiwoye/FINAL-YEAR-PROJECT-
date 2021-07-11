export default class
{
    /**
     * 
     * @param {HTMLTableElement} root The table which will display the csv data
     */
    constructor(root)
    {
        this.root = root;
        
    }
    /**
     * Clears existing data in the table and replaces it with new data.
     *
     * @param {string[][]} data a 2d array of data to be used as the table body 
     * @param {string[][]} headerColumns a 2d array of data to be used as the table body
     */


    update(data, headerColumns = []){
        this.clear();
        this.setHeader(headerColumns);
        this.setBody(data);
    }


    /**
     * clears all contents of table including the header 
     */
    clear() {
        this.root.innerHTML = "";
    }
    /**
     * SETS Table header
     * 
     * @param {string[]}headerColumns list of heading to be used 
     */
    setHeader(headerColumns){
        this.root.insertAdjacentHTML("afterbegin",`
        <thead>
            <tr>
                ${ headerColumns.map( text => `<th> ${text}</th>`).join("") }
            </tr>
        </thead>
       
        
        `);
    }
    /**
     * Sets the table body 
     * @param {string[][]} data a 2d array of data to be used as the table body
     */
    setBody(data)
    {
        const rowsHtml = data.map(row =>{
            return `
            <tr>
                ${  row.map(text =>`<td>${ text }</td>`).join("")}
            </tr>
            `
        })
        
        this.root.insertAdjacentHTML("beforeend", `
            <tbody>
                ${ rowsHtml.join("")}  
            </tbody>
        `)
    }
    
}