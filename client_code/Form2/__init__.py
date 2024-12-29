<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mono Truss Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #234a57;
            color: white;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1em;
            width: 100%;
            text-align: center;
        }

        main {
            display: flex;
            flex-direction: row;
            gap: 20px;
            margin: 20px;
            width: 90%;
            max-width: 1200px;
        }

        section {
            background: white;
            color: black;
            border: 1px solid black;
            border-radius: 8px;
            padding: 20px;
            flex: 1;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h2 {
            margin-top: 0;
            color: white;
        }

        h3 {
            color: white;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        canvas {
            border: 1px solid black;
            width: 100%;
            height: 400px;
        }

        .button-group {
            margin-top: 10px;
            display: flex;
            gap: 10px;
        }

        button {
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button.calculate {
            background-color: #4CAF50;
            color: white;
        }

        button.reset {
            background-color: #f44336;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Mono Truss Calculator</h1>
    </header>

    <main>
        <!-- Input Section -->
        <section>
            <h2>Inputs</h2>
            <h3>Nodes</h3>
            <table id="nodes-table">
                <tr>
                    <th>Node</th>
                    <th>x-Coordinate</th>
                    <th>y-Coordinate</th>
                </tr>
                <tr>
                    <td>A</td>
                    <td><input type="number" value="0"></td>
                    <td><input type="number" value="0"></td>
                </tr>
                <tr>
                    <td>B</td>
                    <td><input type="number" value="5"></td>
                    <td><input type="number" value="0"></td>
                </tr>
                <tr>
                    <td>C</td>
                    <td><input type="number" value="2.5"></td>
                    <td><input type="number" value="5"></td>
                </tr>
            </table>

            <h3>Members</h3>
            <table id="members-table">
                <tr>
                    <th>Member</th>
                    <th>Start Node</th>
                    <th>End Node</th>
                </tr>
                <tr>
                    <td>AC</td>
                    <td>A</td>
                    <td>C</td>
                </tr>
                <tr>
                    <td>BC</td>
                    <td>B</td>
                    <td>C</td>
                </tr>
                <tr>
                    <td>AB</td>
                    <td>A</td>
                    <td>B</td>
                </tr>
            </table>

            <h3>Loads</h3>
            <table id="loads-table">
                <tr>
                    <th>Node</th>
                    <th>Force (Fx)</th>
                    <th>Force (Fy)</th>
                </tr>
                <tr>
                    <td>C</td>
                    <td><input type="number" value="0"></td>
                    <td><input type="number" value="-100"></td>
                </tr>
            </table>

            <div class="button-group">
                <button class="calculate">Calculate</button>
                <button class="reset">Reset</button>
            </div>
        </section>

        <!-- Visualization Section -->
        <section>
            <h2>Truss Diagram</h2>
            <canvas id="truss-canvas"></canvas>
        </section>

        <!-- Results Section -->
        <section>
            <h2>Results</h2>
            <h3>Reactions</h3>
            <table id="reactions-table">
                <tr>
                    <th>Node</th>
                    <th>Reaction Force (Fx)</th>
                    <th>Reaction Force (Fy)</th>
                </tr>
            </table>

            <h3>Member Forces</h3>
            <table id="member-forces-table">
                <tr>
                    <th>Member</th>
                    <th>Force</th>
                    <th>Type</th>
                </tr>
            </table>
        </section>
    </main>

    <script>
        // Placeholder for visualization and calculation logic
        const calculateButton = document.querySelector('.calculate');
        calculateButton.addEventListener('click', () => {
            alert('Calculation logic not yet implemented!');
        });

        const resetButton = document.querySelector('.reset');
        resetButton.addEventListener('click', () => {
            location.reload();
        });
    </script>
</body>
</html>


from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
