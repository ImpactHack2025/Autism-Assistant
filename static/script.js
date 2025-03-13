        let currentActivityIndex = 0;

function showActivity(index) {
    const activity = activities[index];
    const activityDetails = `
        <h2>${activity.activity_name}</h2>
        <p><strong>Format:</strong> ${activity.Activity_format}</p>
        <p><strong>City:</strong> ${activity.city}</p>
        <p><strong>Venue:</strong> ${activity.venue}</p>
        <p><strong>Age Range:</strong> ${activity.age_range.join(' - ')}</p>
        <p><strong>Skills Required:</strong> ${activity.skills_required.join(', ')}</p>
        <p><strong>Sensory Avoid:</strong> ${activity.sensory_avoid.join(', ')}</p>
        <p><strong>Materials to Prepare:</strong> ${activity.materials_to_prepare.join(', ')}</p>
        <p><strong>Steps:</strong></p>
        <ul>
            ${activity.steps.map(step => `<li>${step}</li>`).join('')}
        </ul>
        <p><strong>Safety:</strong> ${activity.safety}</p>
        <p><strong>Date:</strong> ${activity.date}</p>
        <p><strong>Start At:</strong> ${activity.start_at}</p>
        <p><strong>Duration:</strong> ${activity.duration}</p>
        <p><strong>Collaborate Type:</strong> ${activity.collborate_type}</p>
        <p><strong>Cost:</strong> ${activity.cost}</p>
        <p><strong>Contact Person:</strong> ${activity.contact_person}</p>
        <p><strong>Contact Number:</strong> ${activity.contact_number}</p>
    `;
    document.getElementById('activity-details').innerHTML = activityDetails;
}

function showNextActivity() {
    currentActivityIndex = (currentActivityIndex + 1) % activities.length;
    showActivity(currentActivityIndex);
}

function likeActivity() {
    alert(`You liked: ${activities[currentActivityIndex].activity_name}`);
}


async function getRecommendedActivity() {
    try {
        const response = await fetch("/recommend");
        const data = await response.json();
        const index = data.index; // Get the recommended index

        showActivity(index); // Call your function to display the activity
    } catch (error) {
        console.error("Error fetching recommendation:", error);
    }
}

// Call this function when you want to show the recommended activity
getRecommendedActivity();


// Initial display
showActivity(currentActivityIndex);