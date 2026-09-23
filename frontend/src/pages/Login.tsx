import { GoogleLogin } from '@react-oauth/google'

function Login() {
  return (
    <div>
      <h1>Sign in to CareerOS</h1>

      <GoogleLogin
        onSuccess={(credentialResponse) => {console.log(credentialResponse)}}
        onError={() => {console.log('Login Failed')}}
      />
    </div>
  )
}

export default Login