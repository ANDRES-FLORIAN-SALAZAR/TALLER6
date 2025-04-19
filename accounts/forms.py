from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        
class FormularioEliminar(forms.Form):
     # Este formulario se utiliza para eliminar un usuario existente
    usuario = forms.CharField(max_length=150, label="Nombre de usuario")
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    
    ## Validación del formulario
    def clean(self):
        datos_limpiados = super().clean()
        usuario = datos_limpiados.get("usuario")
        contraseña = datos_limpiados.get("contraseña")
        
        # Verificar si el usuario existe y si la contraseña es correcta    
        if not User.objects.filter(username=usuario).exists():
            raise forms.ValidationError("El usuario no existe.")
        
        # Verificar si la contraseña es correcta    
        usuario_obj = User.objects.get(username=usuario)
        if not usuario_obj.check_password(contraseña):
            raise forms.ValidationError("Contraseña incorrecta.")
        
        return datos_limpiados
    
    ## Guardar el usuario eliminado
    def guardar(self, commit=True):
        usuario = self.cleaned_data["usuario"]
        usuario_obj = User.objects.get(username=usuario)
        if commit:
            usuario_obj.delete()
        return usuario_obj

# Este formulario se utiliza para insertar un nuevo usuario
class FormularioInsertar(forms.Form):
    nombre_usuario = forms.CharField(max_length=150, label="Nombre de usuario")
    correo_electronico = forms.EmailField(required=True, label="Correo electrónico")
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    
    def clean(self):
        # Limpiar y validar los datos ingresados
        datos_limpiados = super().clean()
        nombre_usuario = datos_limpiados.get("nombre_usuario")
        correo_electronico = datos_limpiados.get("correo_electronico")
        
        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=nombre_usuario).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
        
        # Verificar si el correo electrónico ya está registrado
        if User.objects.filter(email=correo_electronico).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        
        return datos_limpiados

    def guardar(self, commit=True):
        # Guardar un nuevo usuario con los datos proporcionados
        nombre_usuario = self.cleaned_data["nombre_usuario"]
        correo_electronico = self.cleaned_data["correo_electronico"]
        contraseña = self.cleaned_data["contraseña"]
        
        usuario = User(username=nombre_usuario, email=correo_electronico)
        usuario.set_password(contraseña)
        
        if commit:
            usuario.save()
        return usuario
