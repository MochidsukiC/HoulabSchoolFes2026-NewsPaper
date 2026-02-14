document.addEventListener('DOMContentLoaded', () => {
    updateDate();
});

function updateDate() {
    const dateElement = document.getElementById('current-date');
    if (!dateElement) return;

    const now = new Date();
    
    // Japanese formatting options
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric', 
        weekday: 'short' 
    };
    
    // e.g., 2026年2月13日(金)
    // Note: 'ja-JP' locale automatically handles the format nicely
    const formattedDate = now.toLocaleDateString('ja-JP', options);
    
    dateElement.textContent = formattedDate;
}
