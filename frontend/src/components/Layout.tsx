import { Outlet } from "react-router"

function Layout() {
  return (
    <div>
      <aside>
        CareerOS Navigation
      </aside>

      <main>
        <Outlet />
      </main>
    </div>
  )
}

export default Layout