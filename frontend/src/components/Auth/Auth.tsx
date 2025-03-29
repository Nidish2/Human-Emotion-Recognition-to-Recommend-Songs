import React from "react";
import { SignIn, SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";

const Auth: React.FC = () => (
  <div>
    <SignedIn>
      <UserButton />
    </SignedIn>
    <SignedOut>
      <SignIn />
    </SignedOut>
  </div>
);

export default Auth;
