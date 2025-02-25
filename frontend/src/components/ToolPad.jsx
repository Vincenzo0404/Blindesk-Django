import { extendTheme } from "@mui/material/styles";
import PersonSharpIcon from "@mui/icons-material/PersonSharp";
import AttachMoneySharpIcon from "@mui/icons-material/AttachMoneySharp";
import InventorySharpIcon from "@mui/icons-material/InventorySharp";
import { AppProvider } from "@toolpad/core";
import { DashboardLayout } from "@toolpad/core";
import { PageContainer } from "@toolpad/core";
import Grid from "@mui/material/Grid";
import { Outlet } from "react-router-dom";
import logo from "../assets/logo-trasparente.png";

const NAVIGATION = [
  {
    kind: "header",
    title: "Menu",
  },
  {
    segment: "customer",
    title: "clienti",
    icon: <PersonSharpIcon />,
  },
  {
    segment: "job",
    title: "Commesse",
    icon: <AttachMoneySharpIcon />,
  },
  {
    kind: "divider",
  },
  {
    segment: "products",
    title: "Prodotti",
    icon: <InventorySharpIcon />,
  },
];

const demoTheme = extendTheme({
  colorSchemes: { light: true, dark: true },
  colorSchemeSelector: "class",
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

export default function ToolPad() {
  return (
    <AppProvider
      navigation={NAVIGATION}
      theme={demoTheme}
      branding={{
        logo: <img src={logo} alt="Blindesk logo" />,
        title: "... è troppo ponfia!",
        homeUrl: "/job",
      }}
    >
      <DashboardLayout defaultSidebarCollapsed={true}>
        <PageContainer>
          <Grid container spacing={2}>
            <Outlet />
          </Grid>
        </PageContainer>
      </DashboardLayout>
    </AppProvider>
  );
}
