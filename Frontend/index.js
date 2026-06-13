const sidemenu=document.querySelector('.sidebar-menu');

const teamColors = {
    "McLaren Mercedes": "#FF8000",       
    "Red Bull Racing Honda RBPT": "#0C1E42", 
    "Mercedes": "#00A19B",              
    "Ferrari": "#E10600",                
    "Williams Mercedes": "#005AFF",     
    "Aston Martin Aramco Mercedes": "#006F62", 
    "Alpine Renault": "#0078C1",         
    "Haas Ferrari": "#ffffff90",          
    "Kick Sauber Ferrari": "#52FF00",    
    "Racing Bulls Honda RBPT": "#0000FF" 
};

const gridStructure =[
    { 
        team: "Red Bull Racing Honda RBPT", 
        drivers: ["Max Verstappen", "Yuki Tsunoda"] 
    },
    { 
        team: "McLaren Mercedes", 
        drivers: ["Lando Norris", "Oscar Piastri"] 
    },
    { 
        team: "Ferrari", 
        drivers: ["Charles Leclerc", "Lewis Hamilton"] 
    },
    { 
        team: "Williams Mercedes", 
        drivers: ["Alex Albon", "Carlos Sainz"] 
    },
    { 
        team: "Aston Martin Aramco Mercedes", 
        drivers: ["Fernando Alonso", "Lance Stroll"] 
    },
    { 
        team: "Mercedes", 
        drivers: ["George Russel", "Kimi Antonelli"] 
    },
    { 
        team: "Kick Sauber Ferrari", 
        drivers: ["Nico Hulkenberg", "Gabriel Bortoleto"] 
    },
    { 
        team: "Haas Ferrari", 
        drivers: ["Esteban Ocon", "Oliver Bearman"] 

    },
    { 
        team: "Alpine Renault", 
        drivers: ["Pierre Gasly", "Franco Colapinto", "Jack Doohan"] 

    },
    { team: "Racing Bulls Honda RBPT", drivers: ["Isak Hadjar", "Liam Lawson"] 

    }
];

const teams = ["McLaren Mercedes", "Red Bull Racing Honda RBPT", "Mercedes", "Williams Mercedes", 
    "Aston Martin Aramco Mercedes", "Kick Sauber Ferrari", "Ferrari", "Haas Ferrari", 
    "Alpine Renault", "Racing Bulls Honda RBPT"];

const tracks = ["Australia", "China", "Japan", "Bahrain", "Saudi Arabia", "Miami", "Emilia-Romagna", 
    "Monaco", "Spain"];

function createCust(placeholderText){
    const dropdownFrame=document.createElement('nav');
    dropdownFrame.className='custom-dropdown';
    const toggle=document.createElement('input');
    toggle.type='checkbox';
    toggle.className='dropdown-toggle';
    const header=document.createElement('h2');
    header.textContent=placeholderText;
    const list=document.createElement('ul');
    dropdownFrame.appendChild(toggle);
    dropdownFrame.appendChild(header);
    dropdownFrame.appendChild(list);
    return{
        dropdownFrame, toggle, header, list
    };
}

function generateDrDrop(cont, onsel){
    document.getElementById('card-title').textContent='Driver Analytics';
    const inputGroup=document.createElement('div');
    inputGroup.className='input-group';
    const label=document.createElement('label');
    label.style.color='white';
    label.textContent='Select Driver:';
    inputGroup.appendChild(label);
    const {dropdownFrame, toggle, header, list}=createCust('Select Driver');
    gridStructure.forEach(group=>{
        const groupHeader=document.createElement('li');
        groupHeader.className='dropdown-group-title';
        groupHeader.textContent=group.team;
        if(teamColors[group.team]){
            groupHeader.style.color=teamColors[group.team];
        }
        list.appendChild(groupHeader);
        group.drivers.forEach(driver=>{
            const item=document.createElement('li');
            item.className='dropdown-item';
            const link=document.createElement('a');
            link.href='#';
            link.textContent = driver;
            link.addEventListener('click', (e)=>{
                e.preventDefault();
                header.textContent=driver; 
                toggle.checked=false;    
                if(onsel){
                    onsel(driver);
                }
            });
            item.appendChild(link);
            list.appendChild(item);
        });
    });
    dropdownFrame.appendChild(list);
    inputGroup.appendChild(dropdownFrame);
    cont.appendChild(inputGroup);
}

function generateTrDrop(cont){
    document.getElementById('card-title').textContent='Track Analytics';
    const inputGroup=document.createElement('div');
    inputGroup.className='input-group';
    const label=document.createElement('label');
    label.style.color='white';
    label.textContent='Select Track:';
    inputGroup.appendChild(label);
    const {dropdownFrame, toggle, header, list}=createCust('Select Track');
    tracks.forEach(track =>{
        const item=document.createElement('li');
        item.className='dropdown-item';
        const link=document.createElement('a');
        link.href='#';
        link.textContent=track;
        link.addEventListener('click', (e)=>{
            e.preventDefault();
            header.textContent=track;
            toggle.checked=false;
        });
        item.appendChild(link);
        list.appendChild(item);
    });
    inputGroup.appendChild(dropdownFrame);
    cont.appendChild(inputGroup);
}

function generateTeDrop(cont) {
    document.getElementById('card-title').textContent='Team Analytics';
    const inputGroup=document.createElement('div');
    inputGroup.className='input-group';
    const label=document.createElement('label');
    label.style.color='white';
    label.textContent='Select Team:';
    inputGroup.appendChild(label);
    const {dropdownFrame, toggle, header, list}=createCust('Select Team');
    teams.forEach(team=>{
        const item=document.createElement('li');
        item.className='dropdown-item';
        const link=document.createElement('a');
        link.href='#';
        link.textContent=team;
        if(teamColors[team]){
            link.style.color=teamColors[team];
        }
        link.addEventListener('click', (e)=>{
            e.preventDefault();
            header.textContent=team;
            toggle.checked=false;
        });
        item.appendChild(link);
        list.appendChild(item);
    });
    inputGroup.appendChild(dropdownFrame);
    cont.appendChild(inputGroup);
}

sidemenu.addEventListener('click', (event)=>{
    if(!event.target.classList.contains('menu-btn')){
        return;
    } 
    else{
        let res=document.querySelector('.active');
        if(res){
            res.classList.remove('active');
        }
        event.target.classList.add('active');
        let reportName=event.target.textContent;        
        const cont=document.getElementById('dynamic-selectors');
        const queryCard=document.querySelector('.query-card');
        cont.innerHTML='';
        switch(reportName){
            case 'Overtaker Report':
                document.getElementById('report-name').textContent="Overtaker Report";
                queryCard.style.display='none';
                fetch('http://127.0.0.1:5000/overtaker')
                    .then(response=>{
                        return response.json(); 
                    })
                    .then(serverData=>{
                        const tableBody=document.querySelector('.data-table tbody');
                        const tableHeaders=document.getElementById('head');
                        tableHeaders.innerHTML=`
                        <tr>
                            <th>Track</th>
                            <th>Team</th>
                            <th>Driver</th>
                            <th>Pos</th>
                            <th>Starting Pos</th>
                            <th>Positions Gained</th>
                        </tr>`;
                        tableBody.innerHTML=''; 
                        serverData.forEach(record=>{
                            const tr=document.createElement('tr');
                                tr.innerHTML= `
                                <td>${record.track}</td>
                                <td>${record.team}</td>
                                <td>${record.driver}</td>
                                <td>${record.pos}</td>
                                <td>${record.starting_pos}</td>
                                <td>${record.pos_gained}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    })
                    .catch(error=>console.error("Error fetching F1 data:", error));
                break;
            case 'Efficiency Index':
                document.getElementById('report-name').textContent='Efficiency Index';
                queryCard.style.display='none';
                fetch('http://127.0.0.1:5000/eff')
                    .then(response=>{
                        return response.json(); 
                    })
                    .then(serverData=>{
                        const tableBody=document.querySelector('.data-table tbody');
                        const tableHeaders=document.getElementById('head');
                        tableHeaders.innerHTML=`
                        <tr>
                            <th>Team</th>
                            <th>Driver</th>
                            <th>Rank</th>
                            <th>Volatility Score</th>
                        </tr>`;
                        tableBody.innerHTML=''; 
                        serverData.forEach(record=>{
                            const tr=document.createElement('tr');
                                tr.innerHTML= `
                                <td>${record.team}</td>
                                <td>${record.driver}</td>
                                <td>${record.rank}</td>
                                <td>${record.std}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    })
                    .catch(error=>console.error("Error fetching F1 data:", error));
                break;
            case 'LWMA Rankings':
                document.getElementById('report-name').textContent='LWMA Rankings';
                queryCard.style.display='none';
                fetch('http://127.0.0.1:5000/lwma')
                    .then(response=>{
                        return response.json(); 
                    })
                    .then(serverData=>{
                        const tableBody=document.querySelector('.data-table tbody');
                        const tableHeaders=document.getElementById('head');
                        tableHeaders.innerHTML=`
                        <tr>
                            <th>Team</th>
                            <th>Driver</th>
                            <th>Rank</th>
                        </tr>`;
                        tableBody.innerHTML=''; 
                        serverData.forEach(record=>{
                            const tr=document.createElement('tr');
                                tr.innerHTML= `
                                <td>${record.team}</td>
                                <td>${record.driver}</td>
                                <td>${record.rank}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    })
                    .catch(error=>console.error("Error fetching F1 data:", error));
                break;
            case 'Strong Constructors':
                document.getElementById('report-name').textContent='Strong Constructors';
                queryCard.style.display='none';
                fetch('http://127.0.0.1:5000/constructor')
                    .then(response=>{
                        return response.json(); 
                    })
                    .then(serverData=>{
                        const tableBody=document.querySelector('.data-table tbody');
                        const tableHeaders=document.getElementById('head');
                        tableHeaders.innerHTML=`
                        <tr>
                            <th>Team</th>
                            <th>DNFs</th>
                        </tr>`;
                        tableBody.innerHTML=''; 
                        serverData.forEach(record=>{
                            const tr=document.createElement('tr');
                                tr.innerHTML= `
                                <td>${record.team}</td>
                                <td>${record.dnf}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    })
                    .catch(error=>console.error("Error fetching F1 data:", error));
                break;
                case 'Recovery Driver':
                document.getElementById('report-name').textContent='Recovery Driver';                
                queryCard.style.display='block';
                const tableHeaders=document.getElementById('head');
                        tableHeaders.innerHTML=`
                        <tr>
                            <th>Track</th>
                            <th>Team</th>
                            <th>Driver</th>
                            <th>Pos</th>
                            <th>Starting Pos</th>
                            <th>Points</th>
                        </tr>`;
                const tableBody=document.querySelector('.data-table tbody');
                tableBody.innerHTML=''; 
                generateDrDrop(cont, (selectedDriver)=>{
                const url=`http://127.0.0.1:5000/recovery/${encodeURIComponent(selectedDriver)}`;
                fetch(url)
                    .then(response=>response.json())
                    .then(serverData=>{
                        tableBody.innerHTML=''; 
                        if(serverData.length===0){
                            const tr=document.createElement('tr');
                            tr.innerHTML=`
                                <td colspan="6" style="text-align: center; color: var(--text-muted); padding: 2rem;">
                                    No data available for this driver
                                </td>
                            `;
                            tableBody.appendChild(tr);
                            return;
                        }
                        serverData.forEach(record=>{
                            const tr=document.createElement('tr');
                            tr.innerHTML=`
                                <td>${record.track}</td>
                                <td>${record.team}</td>
                                <td>${record.driver}</td>
                                <td>${record.pos}</td>
                                <td>${record.starting_pos}</td>
                                <td>${record.points}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    })
                    .catch(error=>console.error("Error fetching F1 data:", error));
            });
            break;
        }
    }
});

document.querySelector('.menu-btn.active')?.click();

document.addEventListener('click', (event)=>{
    const openToggle=document.querySelector('.dropdown-toggle:checked');
    if(!openToggle) return;
    const insideDropdown=event.target.closest('.custom-dropdown');
    if(!insideDropdown){
        openToggle.checked=false;
    }
});