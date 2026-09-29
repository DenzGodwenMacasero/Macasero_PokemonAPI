const API_URL = "http://127.0.0.1:5000/pokemon";

const pokemonForm = document.getElementById("pokemon-form");
const pokemonId = document.getElementById("pokemon-id");
const nameInput = document.getElementById("name");
const typeInput = document.getElementById("type");
const levelInput = document.getElementById("level");
const hpInput = document.getElementById("hp");
const imageUrlInput = document.getElementById("image-url");
const submitButton = document.getElementById("submit-button");
const cancelButton = document.getElementById("cancel-button");
const formTitle = document.getElementById("form-title");
const pokemonList = document.getElementById("pokemon-list");
const pokemonDetails = document.getElementById("pokemon-details");
const loading = document.getElementById("loading");
const statusMessage = document.getElementById("status-message");
const refreshButton = document.getElementById("refresh-button");

document.addEventListener("DOMContentLoaded", loadPokemon);

pokemonForm.addEventListener("submit", savePokemon);
cancelButton.addEventListener("click", cancelEdit);
refreshButton.addEventListener("click", loadPokemon);

async function loadPokemon() {
    loading.hidden = false;
    pokemonList.innerHTML = "";

    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Failed to load Pokemon.");
        }

        displayPokemon(data);
    } catch (error) {
        showStatus(error.message, "error");
        pokemonList.innerHTML = "<p>Unable to load Pokemon.</p>";
    } finally {
        loading.hidden = true;
    }
}

function displayPokemon(pokemon) {
    if (pokemon.length === 0) {
        pokemonList.innerHTML = "<p>No Pokemon found.</p>";
        return;
    }

    pokemonList.innerHTML = pokemon.map(p => `
        <div class="pokemon-card">
            <img 
                src="${escapeHtml(p.image_url || 'https://via.placeholder.com/180?text=Pokemon')}" 
                alt="${escapeHtml(p.name)}"
                class="pokemon-image"
                onerror="this.src='https://via.placeholder.com/180?text=No+Image'"
            >

            <h3>${escapeHtml(p.name)}</h3>
            <p><strong>Type:</strong> ${escapeHtml(p.type)}</p>
            <p><strong>Level:</strong> ${p.level}</p>
            <p><strong>HP:</strong> ${p.hp}</p>

            <div class="card-buttons">
                <button onclick="viewPokemon(${p.id})">View</button>
                <button class="edit-button" onclick="editPokemon(${p.id})">Edit</button>
                <button class="delete-button" onclick="deletePokemon(${p.id})">Delete</button>
            </div>
        </div>
    `).join("");
}

async function viewPokemon(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const data = await response.json();

        if (!response.ok) {
            if (response.status === 404) {
                showStatus("Pokemon not found.", "error");
                return;
            }

            throw new Error(data.error || "Failed to load Pokemon.");
        }

        pokemonDetails.innerHTML = `
            <div class="details-box">
                <img 
                    src="${escapeHtml(data.image_url || 'https://via.placeholder.com/220?text=Pokemon')}" 
                    alt="${escapeHtml(data.name)}"
                    class="details-image"
                    onerror="this.src='https://via.placeholder.com/220?text=No+Image'"
                >

                <h3>${escapeHtml(data.name)}</h3>
                <p><strong>ID:</strong> ${data.id}</p>
                <p><strong>Type:</strong> ${escapeHtml(data.type)}</p>
                <p><strong>Level:</strong> ${data.level}</p>
                <p><strong>HP:</strong> ${data.hp}</p>
            </div>
        `;
    } catch (error) {
        showStatus(error.message, "error");
    }
}

async function editPokemon(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const data = await response.json();

        if (!response.ok) {
            if (response.status === 404) {
                showStatus("Pokemon not found.", "error");
                return;
            }

            throw new Error(data.error || "Failed to load Pokemon.");
        }

        pokemonId.value = data.id;
        nameInput.value = data.name;
        typeInput.value = data.type;
        levelInput.value = data.level;
        hpInput.value = data.hp;
        imageUrlInput.value = data.image_url || "";

        formTitle.textContent = "Edit Pokemon";
        submitButton.textContent = "Update Pokemon";
        cancelButton.hidden = false;

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    } catch (error) {
        showStatus(error.message, "error");
    }
}

async function savePokemon(event) {
    event.preventDefault();

    const id = pokemonId.value;

    const pokemonData = {
        name: nameInput.value.trim(),
        type: typeInput.value.trim(),
        level: levelInput.value,
        hp: hpInput.value,
        image_url: imageUrlInput.value.trim()
    };

    const method = id ? "PUT" : "POST";
    const url = id ? `${API_URL}/${id}` : API_URL;

    submitButton.disabled = true;
    submitButton.textContent = id ? "Updating..." : "Adding...";

    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(pokemonData)
        });

        const data = await response.json();

        if (!response.ok) {
            if (response.status === 404) {
                showStatus("Pokemon not found.", "error");
                return;
            }

            if (response.status === 400) {
                showStatus(data.error || "Validation error.", "error");
                return;
            }

            throw new Error(data.error || "Request failed.");
        }

        showStatus(
            id ? "Pokemon updated successfully." : "Pokemon added successfully.",
            "success"
        );

        resetForm();
        await loadPokemon();
    } catch (error) {
        showStatus(error.message, "error");
    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Add Pokemon";
    }
}

async function deletePokemon(id) {
    const confirmed = confirm("Are you sure you want to delete this Pokemon?");

    if (!confirmed) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        const data = await response.json();

        if (!response.ok) {
            if (response.status === 404) {
                showStatus("Pokemon not found.", "error");
                return;
            }

            throw new Error(data.error || "Failed to delete Pokemon.");
        }

        showStatus(data.message || "Pokemon deleted successfully.", "success");

        pokemonDetails.innerHTML = "<p>Select a Pokemon to view its details.</p>";

        await loadPokemon();
    } catch (error) {
        showStatus(error.message, "error");
    }
}

function cancelEdit() {
    resetForm();
}

function resetForm() {
    pokemonForm.reset();
    pokemonId.value = "";
    formTitle.textContent = "Add Pokemon";
    submitButton.textContent = "Add Pokemon";
    cancelButton.hidden = true;
}

function showStatus(message, type) {
    statusMessage.innerHTML = `
        <div class="status ${type}">
            ${escapeHtml(message)}
        </div>
    `;

    setTimeout(() => {
        statusMessage.innerHTML = "";
    }, 4000);
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}