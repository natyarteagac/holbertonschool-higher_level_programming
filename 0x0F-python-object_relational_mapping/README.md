<h1 class="gap">0x0F. Python - Object-relational mapping</h1>


  <ul class="list-group metadata" id="project-metadata">
  <li class="list-group-item">
    <i class="fa fa-folder-open fa-fw"></i>
    <em>Foundations &gt; Higher-level programming &gt; Python</em>
  </li>
<li class="list-group-item">
      <i class="fa fa-user fa-fw"></i> By Guillaume, CTO at Holberton School
</li>
<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/kJjXg3lMFkIpnylTe6Sthg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>Your files will be executed with <code>MySQLdb</code> version <code>1.3.x</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.2.x</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (<code>version 1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use <code>execute</code> with sqlalchemy</li>
</ul>

# Tasks
<h3 class="panel-title">
      0. Get all states
</h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
    <!-- Progress vs Score -->

    <!-- Task Body -->
<p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<h3 class="panel-title">
      1. Filter states
</h3>
<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      2. Filter states by user input
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      3. SQL Injection...
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Wait, do you remember the previous task? Did you test <code>&quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;</code> as an input?</p>

<pre><code>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;
(2, &#39;Arizona&#39;)
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p>What? Empty?</p>

<p>Yes, it&rsquo;s an <a href="/rltoken/f6dtded2o4a09_WEQpLypw" title="SQL injection" target="_blank">SQL injection</a> to delete all records of a table&hellip;</p>

<p>Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (safe from MySQL injection)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      4. Cities by states
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      5. All cities by state
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      6. First state model
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210808T231356Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=931dab0b1fbf60da5bd390588eb855f0c8b49c5c13697a23c6cb27a7eb284a4d" alt="" style="" /></p>

<p>Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:</p>

<ul>
<li><code>State</code> class:

<ul>
<li>inherits from <code>Base</code>  <a href="/rltoken/mafY8fCi8Jav6M8OvCfYvQ" title="Tips" target="_blank">Tips</a></li>
<li>links to the MySQL table <code>states</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can&rsquo;t be null</li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li><strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code></li>
</ul>
    <h3 class="panel-title">
      7. All states via SQLAlchemy
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
   <h3 class="panel-title">
      8. First state
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>The state you display must be the first in <code>states.id</code></li>
<li>You are not allowed to fetch all states from the database before displaying the result</li>
<li>The results must be displayed as they are in the example below</li>
<li>If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line</li>
<li>Your code should not be executed when imported</li>
</ul>
<h3 class="panel-title">
      9. Contains `a`
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      10. Get a state
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)</li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You can assume you have one record with the state name to search</li>
<li>Results must display the <code>states.id</code></li>
<li>If no state has the name you searched for, display <code>Not found</code></li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      11. Add a new state
    </h3>
<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
<p>Write a script that adds the <code>State</code> object &ldquo;Louisiana&rdquo; to the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Print the new <code>states.id</code> after creation</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      12. Update a state
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
<p>Write a script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Change the name of the <code>State</code> where <code>id = 2</code> to <code>New Mexico</code></li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      13. Delete states
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      14. Cities in state
    </h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.</p>

<ul>
<li><code>City</code> class:

<ul>
<li>inherits from <code>Base</code> (imported from <code>model_state</code>)</li>
<li>links to the MySQL table <code>cities</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string of 128 characters and can&rsquo;t be null</li>
<li>class attribute <code>state_id</code> that represents a column of an integer, can&rsquo;t be null and is a foreign key to <code>states.id</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul>

<p>Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      100. City relationship
    </h3>

<div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Improve the files <code>model_city.py</code> and <code>model_state.py</code>, and save them as <code>relationship_city.py</code> and <code>relationship_state.py</code>:</p>

<ul>
<li><code>City</code> class:

<ul>
<li>No change</li>
</ul></li>
<li><code>State</code> class:

<ul>
<li>In addition to previous requirements, the class attribute <code>cities</code> must represent a relationship with the class <code>City</code>. If the <code>State</code> object is deleted, all linked <code>City</code> objects must be automatically deleted. Also, the reference  from a <code>City</code> object to his <code>State</code> should be named <code>state</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul>

<p>Write a script that creates the <code>State</code> &ldquo;California&rdquo; with the <code>City</code> &ldquo;San Francisco&rdquo; from the database <code>hbtn_0e_100_usa</code>: (<code>100-relationship_states_cities.py</code>)</p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      101. List relationship
    </h3>

<div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that lists all <code>State</code> objects, and corresponding <code>City</code> objects, contained in the database <code>hbtn_0e_101_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>The connection to your MySQL server must be to <code>localhost</code> on port <code>3306</code></li>
<li>You must only use one query to the database</li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Results must be sorted in ascending order by <code>states.id</code> and <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
    <h3 class="panel-title">
      102. From city
    </h3>

<div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Write a script that lists all <code>City</code> objects from the database <code>hbtn_0e_101_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use only one query to the database</li>
<li>You must use the <code>state</code> relationship to access to the <code>State</code> object linked to the <code>City</code> object</li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>