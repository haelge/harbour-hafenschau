# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-hafenschau

# >> macros
# << macros

Summary:    Hafenschau
Version:    0.3.3
Release:    1
Group:      Qt/Qt
License:    MIT
URL:        https://github.com/black-sheep-dev/harbour-hafenschau
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-hafenschau.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   sailfish-components-media-qt5
Requires:   sailfish-components-pickers-qt5
Requires:   embedlite-components-qt5 >= 1.21.2
Requires:   qtmozembed-qt5
Requires:   sailfish-components-webview-qt5
Requires:   sailfish-components-webview-qt5-popups
Requires:   sailfish-components-webview-qt5-pickers
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(qt5embedwidget) >= 1.14.9
BuildRequires:  pkgconfig(sailfishsilica)
BuildRequires:  desktop-file-utils

%description
Hafenschau is a native content viewer for german news portal www.tagesschau.de


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/dbus-1/services/harbour.hafenschau.service
# >> files
# << files
