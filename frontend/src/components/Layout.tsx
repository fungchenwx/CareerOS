import { Outlet } from "react-router"

function Layout() {
  return (
    <div>
        <Navbar />
        <div>
            <Sidebar />
            <main>
                <Outlet />
            </main>
        </div>
    </div>
  )
}

export default Layout