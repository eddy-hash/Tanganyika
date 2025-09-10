<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TANGANYIKA student portal</title>

<!-- React CDN -->
<script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>

<link rel="stylesheet" href="styles.css">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>

<div id="root"></div>

<script type="text/babel">
const { useState } = React;

   //main function
function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [message, setMessage] = useState('');

  // Toggle password visibility:
  const togglePassword = () => setShowPassword(!showPassword);

  // Form submit:
  const handleSubmit = (e) => {
    e.preventDefault();

    const usernameValid = /^[A-Z0-9_-]{9,15}$/i.test(username.trim());
    const passwordValid = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/.test(password);

    if(!usernameValid) {
      setMessage("Username must be 9-15 chars: letters, numbers, _ or -");
      return;
    }

    if(!passwordValid) {
      setMessage("Password must be 8+ chars, include uppercase, number & special char");
      return;
    }

    setMessage(
      <span>
        <img src="https://i.ibb.co/gM4Gx43Q/download.png" alt="tick" style={{width:'25px', height:'20px', verticalAlign:'middle'}} /> 
        {' '}Login successfully...
      </span>
    );

    // Optional:
    setUsername('');
    setPassword('');
  };

  return (
    <div className="login-container">
      <h2>The university of TANGANYIKA</h2>
      <img className="logo" src="https://i.ibb.co/LzBmVcq0/school-logo-png.png" alt="school-logo" />

      <form className="login-form" onSubmit={handleSubmit}>
        <div className="input-group">
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)}
            placeholder=""
          />
          <label>Username</label>
        </div>

        <div className="input-group">
          <input 
            type={showPassword ? 'text' : 'password'} 
            value={password} 
            onChange={(e) => setPassword(e.target.value)}
            placeholder=""
          />
          <label>Password</label>
          <span className="material-icons eye-icon" onClick={togglePassword}>
            {showPassword ? 'visibility_off' : 'visibility'}
          </span>
        </div>

        <button type="submit">
          <span className="material-icons">login</span> Login
        </button>
      </form>
      
     <div className="links">
       <a href="#">Forgot Password?</a>
       <a href="#">Register</a>
    </div>

      <p>&copy; 2025. The university of Tanganyika</p>

      <div id="message">{message}</div>
    </div>
  );
}

// Render the React component
ReactDOM.createRoot(document.getElementById('root')).render(<LoginForm />);
</script>

</body>
</html>
