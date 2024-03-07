<h1>Welcome to <i>We Regret to Inform You!</i></h1>


<h3>Code Infrastructure:</h3>


<h4>Main.py:</h4>
<ul>
  <li>-Initializes the game</li>
  <li><i>LATER: Gathers any Save Data</i></li>
</ul>


<h4>Director.py:</h4>
<ul>
  <li>-Initializes tkinter</li>
  <li>Runs the Game Loop:
    <ul>
      <li>Logic (Turn logic, create 5 jobs)</li>
      <li>Output (Creates original UI)</li>
      <li>Input (Player uses actions)</li>
      <li>Logic (Application Logic if applied to jobs)</li>
      <li>Output (Result of any applied jobs)</li>
    </ul>
  </li>
</ul>

<h4>output_services.py</h4>
<ul>
  <li>Creates Turn UI</li>
  <li>Creates Application Result at end of Turn</li>
</ul>
{}
MAIN.PY
	main()
	- call director
	- get last player save (later)

DIRECTOR.PY
	direct()
	- variable to store jobs gotten counter
	- create player (if doesn't exist)
	- create input services
	- create output services
	- game loop - call 5 following functions (while !hired) {}

	update_jobs()
	- generate 5 jobs
	- return 5 job objects

	output_menu(jobs)
	- call outputservices tkinter
	-

	inputs()
	- call inputservices tkinter
	- return dictionary of input values
	{ (html, 4), (css, 5), (internships, [1, 4]) }

	update_applications(jobs, input_dictionary)
	- call application logic
	- generate messages
	- return dictionary { job title, message }
	- if won, 

	output_result( dictionary(job title, message))
	- output messages