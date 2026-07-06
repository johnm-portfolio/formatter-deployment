// Symbol Formatter - Main Script
document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const themeButton = document.getElementById("theme-button");
  
  // Initialize theme from localStorage
  initializeTheme();
  
  // Setup event listeners
  if (themeButton) {
    themeButton.addEventListener("click", changeTheme);
  }
  
  // Only load table data if we're on the symbol table page
  const symbolTable = document.getElementById("symbol-table");
  if (symbolTable) {
    const symbolTableBody = symbolTable.querySelector("tbody");
    const symbolTableHead = symbolTable.querySelector("thead");
    const formulaTable = document.getElementById("formula-table");
    const formulaTableBody = formulaTable.querySelector("tbody");
    const formulaTableHead = formulaTable.querySelector("thead");
    const filterDropdown = document.getElementById("filter");
    let tableRows = [];
    
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
      
      navigator.clipboard.writeText(textToCopy).then(() => {
        showCopyNotification(`"${textToCopy}" copied to clipboard`);
      }).catch(err => {
        console.error("Failed to copy:", err);
        alert(`Failed to copy "${textToCopy}"`);
      });
    }
  }
  
  // Theme Management
  function initializeTheme() {
    const savedTheme = localStorage.getItem("theme") || "dark";
    applyTheme(savedTheme);
  }
  
  function changeTheme() {
    const isDark = body.classList.contains("light-theme") === false;
    const newTheme = isDark ? "light" : "dark";
    applyTheme(newTheme);
    localStorage.setItem("theme", newTheme);
  }
  
  function applyTheme(theme) {
    if (theme === "light") {
      body.classList.add("light-theme");
      updateThemeIcon("☀️");
    } else {
      body.classList.remove("light-theme");
      updateThemeIcon("🌙");
    }
  }
  
  function updateThemeIcon(icon) {
    if (themeButton) {
      const iconSpan = themeButton.querySelector(".theme-icon");
      if (iconSpan) {
        iconSpan.textContent = icon;
      }
    }
  }
  
  // Copy notification
  function showCopyNotification(message) {
    // Create a simple toast-like notification
    const notification = document.createElement("div");
    notification.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: rgba(0, 217, 255, 0.9);
      color: #0f1419;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 600;
      z-index: 1000;
      animation: slideIn 0.3s ease-in-out;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    // Remove after 2 seconds
    setTimeout(() => {
      notification.style.animation = "slideOut 0.3s ease-in-out";
      setTimeout(() => {
        document.body.removeChild(notification);
      }, 300);
    }, 2000);
  }

  const fileInput = document.getElementById("fileInput");
  const uploadBtn = document.getElementById("uploadBtn");
  const statusText = document.getElementById("statusText");

  if (!uploadBtn) return;

  uploadBtn.addEventListener("click", async () => {
      const file = fileInput.files[0];

      if (!file) {
          statusText.textContent = "Please select a file first.";
          return;
      }

      statusText.textContent = "Uploading...";

      const formData = new FormData();
      formData.append("file", file);

      try {
          const response = await fetch("/format", {
              method: "POST",
              body: formData
          });

          if (!response.ok) {
              throw new Error("Upload failed");
          }

          const blob = await response.blob();

          const url = window.URL.createObjectURL(blob);
          const a = document.createElement("a");

          a.href = url;
          a.download = "formatted.md";
          document.body.appendChild(a);
          a.click();
          a.remove();

          statusText.textContent = "Download ready!";
      } catch (err) {
          console.error(err);
          statusText.textContent = "Something went wrong.";
      }
  });
});


// Add animation styles
const style = document.createElement("style");
style.textContent = `
  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  @keyframes slideOut {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(100%);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);