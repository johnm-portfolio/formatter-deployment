// Made by John McNally

document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  
  const symbolTable = document.getElementById("symbol-table");
  const symbolTableBody = symbolTable.querySelector("tbody");
  const symbolTableHead = symbolTable.querySelector("thead");
  const formulaTable = document.getElementById("formula-table");
  const formulaTableBody = formulaTable.querySelector("tbody");
  const formulaTableleHead = formulaTable.querySelector("thead");

  const themeButton = document.getElementById("theme-button");
  const themeButtonImg = themeButton.querySelector("img");
  const filterDropdown = document.getElementById("filter");

  let tableRows = [];

  themeButton.addEventListener("click", changeTheme);
  filterDropdown.addEventListener("change", applyFilter);
  symbolTableBody.addEventListener("click", handleTableClick);

  init().catch((err) => {
    console.error(err);
    alert("Could not load symbol table data.");
  });

  async function init() {
    const response = await fetch("./data/symbols.json");
    if (!response.ok) {
      throw new Error(`Failed to load symbols.json: ${response.status}`);
    }

    const data = await response.json();
    renderSymbolTable(data.symbols || []);
    tableRows = Array.from(symbolTableBody.querySelectorAll("tr"));

    renderFormulaTable(data.formulae || []);
    applyFilter();
  }

  function renderSymbolTable(symbols) {
    symbolTableBody.innerHTML = "";

    for (const item of symbols) {
      const tr = document.createElement("tr");
      tr.className = item.categories.join(" ");
      tr.dataset.categories = item.categories.join(" ");
      tr.dataset.copy = item.copy ?? item.output;

      const symbolTd = document.createElement("td");
      symbolTd.className = "symbol";
      symbolTd.innerHTML = item.output;

      const reprTd = document.createElement("td");
      reprTd.textContent = item.inputs.join(" or ");

      const descTd = document.createElement("td");
      descTd.textContent = item.description || "";

      tr.appendChild(symbolTd);
      tr.appendChild(reprTd);
      tr.appendChild(descTd);

      symbolTableBody.appendChild(tr);
    }
  }

  function renderFormulaTable(formulae) {
    formulaTableBody.innerHTML = "";

    for (const rule of formulae) {
      const tr = document.createElement("tr");

      const patternTd = document.createElement("td");
      patternTd.textContent = rule.pattern;

      const replacementTd = document.createElement("td");
      replacementTd.textContent = rule.replacement;

      const descTd = document.createElement("td");
      descTd.textContent = rule.description || "";

      tr.appendChild(patternTd);
      tr.appendChild(replacementTd);
      tr.appendChild(descTd);

      formulaTableBody.appendChild(tr);
    }
  }

  function changeTheme() {
    const isDark = body.className === "dark-theme-main";
    const themeStyle = isDark ? "light" : "dark";

    body.className = `${themeStyle}-theme-main`;
    symbolTableBody.className = `${themeStyle}-theme-table-body`;
    symbolTableHead.className = `${themeStyle}-theme-table-heading`;
    formulaTableBody.className = `${themeStyle}-theme-table-body`;
    formulaTableHead.className = `${themeStyle}-theme-table-heading`;
    themeButton.className = `${themeStyle}-theme-button`;
    themeButtonImg.src = `images/${themeStyle}_theme_button_icon.png`;
  }

  function applyFilter() {
    const filterValue = filterDropdown.value;

    for (const row of tableRows) {
      if (filterValue === "all") {
        row.classList.remove("hidden");
        continue;
      }

      const categories = (row.dataset.categories || "").split(" ").filter(Boolean);
      if (categories.includes(filterValue)) {
        row.classList.remove("hidden");
      } else {
        row.classList.add("hidden");
      }
    }
  }

  function handleTableClick(event) {
    const cell = event.target.closest(".symbol");
    if (!cell) return;

    const row = cell.closest("tr");
    const textToCopy = row?.dataset.copy || cell.textContent.trim();

    navigator.clipboard.writeText(textToCopy);
    alert(`"${textToCopy}" copied to clipboard`);
  }

  function stripHtml(html) {
    const div = document.createElement("div");
    div.innerHTML = html;
    return div.textContent || div.innerText || "";
  }
});